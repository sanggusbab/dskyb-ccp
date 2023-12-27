# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Float, Integer, TIMESTAMP, Time, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AssignmentTbl(Base):
    __tablename__ = 'assignment_tbl'

    index = Column(Integer, primary_key=True)
    device_id = Column(Integer, nullable=False)
    task_subgroup_code = Column(Integer, nullable=False)
    take_yn = Column(CHAR(1), nullable=False)
    insrt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class AvailableEdgeDeviceTbl(Base):
    __tablename__ = 'available_edge_device_tbl'

    index = Column(Integer, primary_key=True)
    device_id = Column(Integer, nullable=False)
    use_yn = Column(CHAR(1), nullable=False)
    rect_left = Column(Float, nullable=False)
    rect_top = Column(Float, nullable=False)
    rect_right = Column(Float, nullable=False)
    rect_bottom = Column(Float, nullable=False)
    motion_code = Column(CHAR(4), nullable=False)
    insrt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class MotionCodeInfoTbl(Base):
    __tablename__ = 'motion_code_info_tbl'

    motion_code = Column(Integer, primary_key=True)
    description = Column(CHAR(255), nullable=False)


class ScoreRequestQueueTbl(Base):
    __tablename__ = 'score_request_queue_tbl'

    request_id = Column(Integer, primary_key=True)
    device_id = Column(Integer, nullable=False)
    task_subgroup_code = Column(Integer, nullable=False)
    insrt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ScoreTbl(Base):
    __tablename__ = 'score_tbl'

    index = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    expected_score = Column(Integer, nullable=False)
    expected_time = Column(Time, nullable=False)
    insrt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updt_ts = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


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