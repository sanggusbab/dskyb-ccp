# coding: utf-8
from sqlalchemy import Column, Float, DATETIME, CHAR, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class available_edge_device_tbl(Base):
    __tablename__ = 'available_edge_device_tbl'

    index = Column(INTEGER(11), primary_key=True)
    device_id = Column(INTEGER(11), nullable=False)
    use_yn = Column(CHAR(1), nullable=False)
    rect_left = Column(Float, nullable=False)
    rect_top = Column(Float, nullable=False)
    rect_right = Column(Float, nullable=False)
    rect_bottom = Column(Float, nullable=False)
    motion_code = Column(CHAR(4), nullable=False)
    insrt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp()"))
    updt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))

class subgroup_detail_tbl(Base):
    __tablename__ = 'subgroup_detail_tbl'

    index = Column(INTEGER(11), primary_key=True)
    task_subgroup_code = Column(INTEGER(11))
    location_x = Column(Float)
    location_y = Column(Float)
    motion_code = Column(INTEGER(11))
    sequence = Column(INTEGER(11))
    requested_start_time = Column(DATETIME)
    insrt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp()"))
    updt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))

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