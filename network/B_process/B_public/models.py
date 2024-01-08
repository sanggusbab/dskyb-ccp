# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Float, Integer, TIMESTAMP, Time, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class MotionCodeInfoTbl(Base):
    __tablename__ = 'motion_code_info_tbl'

    motion_code = Column(Integer, primary_key=True)
    description = Column(CHAR(255), nullable=False)

class SubgroupDetailTbl(Base):
    __tablename__ = 'subgroup_detail_tbl'

    index = Column(Integer, primary_key=True)
    task_subgroup_code = Column(Integer, nullable=False)
    location_x = Column(Float, nullable=False)
    location_y = Column(Float, nullable=False)
    motion_code = Column(Integer, nullable=False)
    sequence = Column(Integer, nullable=False)
    requested_start_time = Column(DateTime)
    insrt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SubgroupInfoTbl(Base):
    __tablename__ = 'subgroup_info_tbl'

    index = Column(Integer, primary_key=True)
    task_id = Column(Integer, nullable=False)
    user_id = Column(CHAR(255), nullable=False)
    task_group = Column(Integer, nullable=False)
    task_subgroup_code = Column(Integer, nullable=False)
    insrt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
