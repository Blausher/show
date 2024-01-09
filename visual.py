from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import config
from db_manager import DBManager


class Keyboards:  # клава
    def __init__(self):
        self.visual = None
        self.BD = DBManager()

    def set_button(self, name):
        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        self.visual = ReplyKeyboardMarkup(True, True)
        btn_1 = self.set_button('Расписание')
        btn_2 = self.set_button('Тренировки')
        btn_3 = self.set_button('Цены')
        btn_4 = self.set_button('Корты')
        btn_5 = self.set_button('info')
        btn_6 = self.set_button('Отзыв')

        self.visual.row(btn_1)
        self.visual.row(btn_2, btn_3)
        self.visual.row(btn_5)
        # self.visual.row(btn_6)
        return self.visual

    def schedule_menu(self):
        self.visual = ReplyKeyboardMarkup(True, True)
        #todo добавить кнопку "кто идет на тренировку? -> делает sql запрос
        #todo клиенты которые идут на тренировки согласно времени ники списком

        btn_1 = self.set_button('<<')
        self.visual.row(btn_1)
        return self.visual

    def trainings_menu(self):
        self.visual = ReplyKeyboardMarkup(True, True)
        btn_1 = self.set_button('<<')
        self.visual.row(btn_1)
        return self.visual

    def prices_menu(self):
        self.visual = ReplyKeyboardMarkup(True, True)
        btn_1 = self.set_button('<<')
        self.visual.row(btn_1)
        return self.visual

    def courts_menu(self):  # not needed right now
        self.visual = ReplyKeyboardMarkup(True, True)
        btn_1 = self.set_button('<<')
        self.visual.row(btn_1)
        return self.visual

    def info_menu(self):
        self.visual = ReplyKeyboardMarkup(True, True)
        btn_1 = self.set_button('<<')
        self.visual.row(btn_1)
        return self.visual

    def feedback_menu(self):  # not needed right now
        self.visual = ReplyKeyboardMarkup(True, True)
        btn_1 = self.set_button('<<')
        self.visual.row(btn_1)
        return self.visual

    def set_inline_button(self, name, tr_id): #инлайн кнопка
        return InlineKeyboardButton(str(name), callback_data = str(tr_id)) #на каждой кнопке появляется название товара
    # callback_data=str(name.id)

    def schedule_rows(self):
        self.visual = InlineKeyboardMarkup(row_width=1)

        for row in self.BD.select_all_future_trainings():
            row_list = [row.weekday1,
                        row.date1.strftime('%m.%d'),
                        row.time1.strftime('%H:%M'),
                        row.location,
                        row.group_lvl]
            row_list1 = ' '.join(str(e) for e in row_list)

            self.visual.add(self.set_inline_button(row_list1, row.training_id))

        return self.visual


    def set_inline_button_info(self):
        self.visual = InlineKeyboardMarkup(row_width=1)

        texts = ["\U0001F4CD Корты в Москве",
                 "\U0001F4A1 Общая детальная информация",
                 "\U0001F4E9 Оставить отзыв"]
        links = ['https://weikath.notion.site/Lashmanov-9da9318f4a424061ad6212b32d35041c?pvs=4',
                 'http://simp.ly/p/rylC7c',
                 'https://docs.google.com/forms/d/e/1FAIpQLSfORe4aKQzX01NjPUj4tnoK_TZUrq6_crypLbAHQOCUE3x-IQ/viewform?usp=sf_link']

        for txt, link in zip(texts, links):
            self.visual.add(InlineKeyboardButton(text = txt, url= link))

        return self.visual






