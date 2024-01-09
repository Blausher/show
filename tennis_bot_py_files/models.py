from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy import Date, Time, DateTime
from dbcore import Base


class schedule(Base):
    __tablename__ = 'schedule'

    training_id = Column(Integer, primary_key=True)
    weekday1 = Column(String(20))
    date1 = Column(Date)
    time1 = Column(Time, nullable=False)
    lasts_hours = Column(Integer)
    location = Column(String(250), nullable=False)
    group_lvl = Column(Integer)


class clients(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(250))
    tgnick = Column(String(250))
    phone = Column(String(250))
    group_lvl = Column(Integer)
    payment = Column(Integer)
    payment_date = Column(Date)
    trainings_left = Column(Integer)


class clid_trid(Base):
    __tablename__ = 'clid_trid'
    #     __table_args__ = (PrimaryKeyConstraint('application_essay_id', 'theme_essay_id'),)
    match_id = Column(Integer, primary_key=True)
    clid = Column(Integer, ForeignKey("clients.client_id"))  # ForeignKey("clients.client_id")
    trid = Column(Integer, ForeignKey("schedule.training_id"))  # ForeignKey("schedule.training_id")