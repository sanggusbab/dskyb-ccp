# coding: utf-8
from sqlalchemy import Column, Float
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class tbl(Base):
    __tablename__ = 'tbl'

    index = Column(INTEGER(11), primary_key=True)
    task_id = Column(INTEGER(11))
    position_x = Column(Float)
    position_y = Column(Float)


class edge(Base):
    __tablename__ = 'edge'

    index = Column(INTEGER(11), primary_key=True)
    edge_id = Column(INTEGER(11))
    edge_x = Column(Float)
    edge_y = Column(Float)