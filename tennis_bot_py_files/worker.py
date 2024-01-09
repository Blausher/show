import abc  # абстрактные классы
from visual import Keyboards  # клава
from messages import MESSAGES
import config
from db_manager import DBManager


class Worker(metaclass=abc.ABCMeta):  # тут лежат Keyboards и bot
    def __init__(self, bot):
        self.bot = bot  # получаем объект бота
        self.keyboards = Keyboards()  # инициализируем разметку кнопок
        self.BD = DBManager()


    @abc.abstractmethod
    def handle(self):
        pass


# ===========================================WORKER COMMANDS=========================================================
class Worker_commands(Worker):  # Keyboards, bot + pressed_button + handle
    def __init__(self, bot):
        super().__init__(bot)

        self.tg_nickname = None
        self.tg_first_name = None

    def pressed_button_start(self, message):
        self.tg_nickname = message.from_user.username
        self.tg_first_name = message.from_user.first_name

        self.bot.send_message(
            message.chat.id,
            f'{self.tg_first_name}, Привет! Твой ник: @{self.tg_nickname}.'
            f' Я тебя запомню. Это школа тенниса бла бла, и я телеграм бот, с помощью которого '
            f'тебе просто будет легче жить!',
            reply_markup=self.keyboards.start_menu())

    #     получить tg nickname и записать в БД при регистрации и тд
    #     https://docs.python-telegram-bot.org/en/v20.5/telegram.user.html#telegram.User

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(message)
            if message.text == '/start':
                self.pressed_button_start(message)


# ===========================================TEXT HANDLER==========================================================
class TextHandler(Worker):  # Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_schedule(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['schedule'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.schedule_menu())

        self.bot.send_message(message.chat.id, 'Инфо про расписание ',
                              reply_markup=
                              self.keyboards.schedule_rows())

    def pressed_btn_trainings(self, message):  # not needed right now
        self.bot.send_message(message.chat.id, MESSAGES['trainings'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.trainings_menu())

    def pressed_btn_prices(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['prices'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.prices_menu())

    def pressed_btn_courts(self, message):  # not needed right now
        self.bot.send_message(message.chat.id, MESSAGES['courts'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.courts_menu())

    def pressed_btn_info(self, message):

        self.bot.send_message(message.chat.id, MESSAGES['info'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.info_menu())

        self.bot.send_message(message.chat.id, 'Все нужные ссылки:',
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_button_info())



    def pressed_btn_feedback(self, message):  # not needed right now
        self.bot.send_message(message.chat.id, MESSAGES['feedback'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.feedback_menu())

    def pressed_btn_back(self, message):
        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):

            # ---------------Главное меню------------------------
            if message.text == config.KEYBOARD['Расписание']:
                self.pressed_btn_schedule(message)

            if message.text == config.KEYBOARD['Тренировки']:  # not needed right now
                self.pressed_btn_trainings(message)

            if message.text == config.KEYBOARD['Цены']:
                self.pressed_btn_prices(message)

            if message.text == config.KEYBOARD['Корты']:
                self.pressed_btn_courts(message)

            if message.text == config.KEYBOARD['info']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['Отзыв']:  # not needed right now
                self.pressed_btn_feedback(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)


# ================================== INLINE =========================================================================
class HandlerInlineQuery(Worker):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на inline-кнопок
    """
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_row_in_schedule(self, call, tg_nick, tg_first_name):  # Обрабатывает нажатия inline-кнопок

        # тут проверяем, а есть ли этот ник уже в базе:
        if self.BD.check_if_user_in_DB(tg_nick) == True:
            pass
        else:
            self.BD.add_user(tg_first_name, tg_nick)  # а тут уже добавляем в базу если этого ника еще в ней нет

        # посылаем сообщение
        self.bot.answer_callback_query(
            call.id,
            MESSAGES['reg_for_training_message'],
            show_alert=True)

    def handle(self):
        # обработчик(декоратор) запросов от нажатия на inline кнопки
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            tg_nick = call.from_user.username
            tg_first_name = call.from_user.first_name

            training_id = int(call.data) #training id in schedule реальное

            self.pressed_row_in_schedule(call, tg_nick, tg_first_name) #добавляем юзера или нет если он уже есть в базе

            self.BD.add_clid_trid_row(clid1 = self.BD.get_user_id(tg_nick), trid1=training_id) #человек записался на тренировку






# ====================================WORKER MAIN==========================================================
class Worker_main:
    def __init__(self, bot):
        self.bot = bot  # получаем нашего бота
        self.handler_commands = Worker_commands(self.bot)
        self.handler_text = TextHandler(self.bot)
        self.handler_inline = HandlerInlineQuery(self.bot)

    def handle(self):
        self.handler_commands.handle()
        self.handler_text.handle()
        self.handler_inline.handle()
