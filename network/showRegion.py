from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

# Database connection information
user = "dskyb-team"
pwd = "0e3!ca#@532#$!FS2c68"
host = "35.76.155.156"
port = 3306
DB_NAME = "dskybdb"

# MySQL connection URL
DB_URL = f"mysql+pymysql://{user}:{quote(pwd)}@{host}:{port}/{DB_NAME}"

# SQLAlchemy Base
Base = declarative_base()

# Define your table model
class AvailableEdgeDevice(Base):
    __tablename__ = 'available_edge_device_tbl'

    index = Column(Integer, primary_key=True)
    device_id = Column(Integer)
    use_yn = Column(String(1))
    rect_left = Column(Float)
    rect_top = Column(Float)
    rect_right = Column(Float)
    rect_bottom = Column(Float)
    motion_code = Column(Integer)

# Your engine connection class
class EngineConn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)
    
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn

# Usage example
if __name__ == "__main__":
    # Create tables if not exists
    Base.metadata.create_all(EngineConn().engine)

    # Use the session
    session = EngineConn().sessionmaker()

    # Example query
    devices = session.query(AvailableEdgeDevice).all()
    fig, ax = plt.subplots()

    # List of colors
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

    # Plot each device's box with a different color
    for i, device in enumerate(devices):
        if(i%3 == 0):
            color = random.choice(colors)  # Randomly select a color from the list
            rect = patches.Rectangle((device.rect_left/1000, device.rect_bottom/1000), 
                                    device.rect_right/1000 - device.rect_left/1000, 
                                    device.rect_top/1000 - device.rect_bottom/1000, 
                                    linewidth=1, edgecolor=color, facecolor='none', label=f'Device {int(i/3) + 1}')
            ax.add_patch(rect)

    # Set axis labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Set the aspect of the plot to be equal
    ax.set_aspect('equal', 'box')

    # Add legend outside the plot
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Show the plot
    plt.show()

    # Close the session
    session.close()
