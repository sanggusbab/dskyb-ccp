# coding: utf-8
from sqlalchemy import CHAR, Column
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class tbl(Base):
    __tablename__ = 'tbl'

    index = Column(INTEGER(11), primary_key=True)
    task_id = Column(INTEGER(11))
    position_x = Column(FLOAT)
    position_y = Column(FLOAT)


class edge(Base):
    __tablename__ = 'edge'

    index = Column(INTEGER(11), primary_key=True)
    edge_id = Column(INTEGER(11))
    edge_x = Column(FLOAT)
    edge_y = Column(FLOAT)