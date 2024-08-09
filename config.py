import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:p@stgress@localhost:5433/tripdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    