from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_mail import Mail
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect(app)
mail = Mail(app)
db = SQLAlchemy(app)


from mainapp.controllers import ssh, views, forms
