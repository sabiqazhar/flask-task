import os
from sqlalchemy import create_engine, text

basedir = os.path.abspath(os.path.dirname(__file__))
DB_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

engine = create_engine(DB_URI)

class Config:
    SECRET_KEY = 'admin'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class MailConfig:
    MAIL_SERVER = 'TEST'
    MAIL_PORT = 432
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'projtanjoy@gmail.com'
    MAIL_PASSWORD = '*****'