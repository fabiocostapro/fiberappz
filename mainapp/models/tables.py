from mainapp import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(40))
    cpf = db.Column(db.String(14), unique=True)
    company = db.Column(db.String(40), unique=True)
    cnpj = db.Column(db.String(18), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(93))
    admin = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, name, cpf, company, cnpj, email, password, admin, created_date):
        self.username = username
        self.name = name
        self.username = username
        self.cpf = cpf
        self.company = company
        self.cnpj = cnpj
        self.email = email
        self.password = self.__create_password(password)

    def __repr__(self):
        return "<User %r>" % self.username


class Olt(db.Model):
    __tablename__ = "olts"

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), unique=True)
    port = db.Column(db.String(40))
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"))
