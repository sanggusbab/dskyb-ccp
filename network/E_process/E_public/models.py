# coding: utf-8
from sqlalchemy import Column, Float, DATETIME, CHAR, TIME, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class subgroup_info_tbl(Base):
    __tablename__ = 'subgroup_info_tbl'

    index = Column(INTEGER(11), primary_key=True)
    task_id = Column(INTEGER(11), nullable=False)
    user_id = Column(CHAR(255), nullable=False)
    task_group = Column(INTEGER(11), nullable=False)
    task_subgroup_code = Column(INTEGER(11), nullable=False)
    insrt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp()"))
    updt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))

class assignment_tbl(Base):
    __tablename__ = 'assignment_tbl'

    index = Column(INTEGER(11), primary_key=True)
    device_id = Column(INTEGER(11), nullable=False)
    task_subgroup_code = Column(INTEGER(11), nullable=False)
    take_yn = Column(CHAR(1), nullable=False)
    insrt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp()"))
    updt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))

class score_request_queue_tbl(Base):
    __tablename__ = 'score_request_queue_tbl'

    request_id = Column(INTEGER(11), primary_key=True)
    device_id = Column(INTEGER(11), nullable=False)
    task_subgroup_code = Column(INTEGER(11), nullable=False)
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
    
class score_tbl(Base):
    __tablename__ = 'score_tbl'

    index = Column(INTEGER(11), primary_key=True)
    request_id = Column(INTEGER(11), nullable=False)
    expected_score = Column(INTEGER(11), nullable=False)
    expected_time = Column(TIME, nullable=False)
    insrt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp()"))
    updt_ts = Column(DATETIME, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))

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