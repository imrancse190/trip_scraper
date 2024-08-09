from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config


Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Float)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String)
    price = Column(String)
    image_paths = Column(String)

DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
