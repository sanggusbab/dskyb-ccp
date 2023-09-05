# 기존에 존재하는 database를 sqlalchemy를 이용해 연결해주는 파일
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secret import USER, PW, HOST, PORT, DB_NAME

DB_URL = f'mysql+pymysql://{USER}:{PW}@{HOST}:{PORT}/{DB_NAME}'

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)
    
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    def connection(self):
        conn = self.engine.connect()
        return conn