# coding: utf-8
from sqlalchemy import CHAR, Column
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class available_edge_device_tbl(Base):
    __tablename__ = 'available_edge_device_tbl'

    index = Column(INTEGER(11), primary_key=True)
    device_id = Column(INTEGER(11))
    rect_top = Column(FLOAT)
    rect_bottom = Column(FLOAT)
    rect_left = Column(FLOAT)
    rect_right = Column(FLOAT)