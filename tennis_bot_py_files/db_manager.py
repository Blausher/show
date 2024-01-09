from datetime import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import mysql #кажется надо сменить интерпретатора, тут не видит mysql
# from dbcore import Base
import config

from models import schedule
from models import clients
from models import clid_trid



class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs): #принимает атрибуты подчиненного класса
        # cls = DBManager, name - название, bases - все предки, attrs - атрибуты подчиненного класса
        super().__init__(name, bases, attrs)
        cls.__instance = None  #изначально объект подчиненного класса ссылается на None
                               #когда происходит создание класса и возврат его экземпляра
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):  #Класс менеджер для работы с БД DBManager находится под управлением класса Sindleton, те можем контролировать DBManager с помощью Singleton
    def __init__(self):  #инициализация сессии и подключение к БД
        # self.engine = create_engine(config.DATABASE)  #указывается путь до БД
        self.engine = create_engine("mysql+mysqlconnector://sql11646442:yJqwfBEZEy@sql11.freesqldatabase.com/sql11646442",
                               echo=True)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        # if not path.isfile(config.DATABASE):
        #     Base.metadata.create_all(self.engine) #если БД еще нет, то создаем ее

    def close(self):
        """ Закрывает сессию """
        return self._session.close()

    def select_all_future_trainings(self):
        result = self._session.query(schedule).filter(dt.now().date() <= schedule.date1) #todo !!!
        self.close() #завершаем сессию
        return result

    def check_if_user_in_DB(self, tg_nickname):
        tg_nickname = '@'+tg_nickname

        l = []
        for row in self._session.query(clients.client_id, clients.tgnick):
            row_list = list(row)
            l.append(row_list)

        nicks_list = []
        for el in l:
            tgnick = el[-1]
            nicks_list.append(tgnick)

        if tg_nickname in nicks_list:
            answer = True
        else:
            answer = False

        self.close()
        return answer

    def add_user(self, first_name, tg_nickname):
        new_user = clients(name = first_name, tgnick = f'@{tg_nickname}')
        self._session.add(new_user)
        self._session.commit()
        self.close()


    def get_user_id(self, tg_nickname):
        for row in self._session.query(clients.client_id).filter(clients.tgnick == '@'+tg_nickname):
            listed_row = list(row)
        ans = listed_row[0]
        return ans


    def add_clid_trid_row(self, clid1, trid1):

        clid_trid_row = clid_trid(clid=clid1, trid=trid1)

        self._session.add(clid_trid_row)
        self._session.commit()
        self.close()









