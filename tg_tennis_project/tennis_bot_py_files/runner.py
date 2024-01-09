from telebot import TeleBot
import config
from worker import Worker_main


class TelegramBot:
    def __init__(self):
        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.worker = Worker_main(self.bot)  # инициализируем обработчик событий

    def run_bot(self):
        self.worker.handle()  # обработчик событий
        self.bot.polling(none_stop=True)  # запуск бота (работа в режиме нон-стоп)


bot = TelegramBot()
bot.run_bot()
