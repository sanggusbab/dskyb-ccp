# coding: utf-8
from sqlalchemy import CHAR, Column
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class tbl1(Base):
    __tablename__ = 'tbl1'

    index = Column(INTEGER(11), primary_key=True)
    edge_id = Column(INTEGER(11))
    rect_left = Column(FLOAT)
    rect_top = Column(FLOAT)
    rect_right = Column(FLOAT)
    rect_bottom = Column(FLOAT)