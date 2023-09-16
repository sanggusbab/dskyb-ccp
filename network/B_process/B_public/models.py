# coding: utf-8
from sqlalchemy import CHAR, Column
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Program(Base):
    __tablename__ = 'program'

    program_cd = Column(CHAR(4), primary_key=True)
    program = Column(CHAR(20))
    teacher = Column(CHAR(10))
    price = Column(INTEGER(10))


class Register(Base):
    __tablename__ = 'register'

    id = Column(INTEGER(5), primary_key=True)
    user_id = Column(INTEGER(3))
    name = Column(CHAR(10))
    program_cd = Column(CHAR(4))
    pay = Column(CHAR(1))
