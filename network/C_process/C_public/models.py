# coding: utf-8
from sqlalchemy import Column, Float, DATETIME
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class subgroup_detail_tbl(Base):
    __tablename__ = 'subgroup_detail_tbl'

    index = Column(INTEGER(11), primary_key=True)
    task_subgroup_code = Column(INTEGER(11))
    location_x = Column(Float)
    location_y = Column(Float)
    motion_code = Column(INTEGER(11))
    sequence = Column(INTEGER(11))
    requested_start_time = Column(DATETIME)
    insrt_t = Column(DATETIME)
    updt_ts = Column(DATETIME)

class B2(Base):
    __tablename__ = 'B2'

    index = Column(INTEGER(11), primary_key=True)
    task_group = Column(INTEGER(11))
    location_x = Column(Float)
    location_y = Column(Float)
    motion_code = Column(INTEGER(11))
    task_subgroup_code = Column(INTEGER(11))


class C1(Base):
    __tablename__ = 'C1'

    index = Column(INTEGER(11), primary_key=True)
    device_id = Column(INTEGER(11))
    task_subgroup_code = Column(INTEGER(11))