import os


class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = "fiberappz@gmail.com"
    MAIL_PASSWORD = os.environ.get("PASSWORD_EMAIL_FI")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://fiberapp_user:quil1472@localhost/fiberapp_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
