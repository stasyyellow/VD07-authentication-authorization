import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'peshera-fignya'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
