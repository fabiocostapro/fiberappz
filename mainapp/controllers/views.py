#! /usr/bin/python3
# -*- coding: utf-8 -*-

# from helper import date_format
# from flask import make_response
from mainapp import app
from mainapp import mail
from mainapp import db
from mainapp.models.tables import User
from mainapp.controllers.forms import UserCreateForm
from mainapp.controllers.forms import LoginForm
from mainapp.controllers.ssh import uptime, ls

from flask import render_template
from flask import request
from flask import flash
from flask import session
from flask import url_for
from flask import redirect

from flask_mail import Message
import json


# @app.before_request
# def before_request():
#     user_pages = ["index", "ssh_request"]
#     admin_pages = ["admin", "user_create", "user_edit", "user_delete"]
#     if "username" not in session and request.endpoint in user_pages:
#         return redirect(url_for("login"))
#     elif "username" in session and request.endpoint in ["login"]:
#         return redirect(url_for("index"))
#     elif "admin" not in session and request.endpoint in admin_pages:
#         return redirect(url_for("index"))


@app.after_request
def after_request(response):
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("page-404.html"), 404


# @app.route("/admin")
# def admin():
#     return render_template("admin.html")


# @app.route("/user-create", methods=["GET", "POST"])
# def user_create():
#     user_create_form = UserCreateForm(request.form)
#     if request.method == "POST" and user_create_form.validate():
#         user = User(user_create_form.username.data,
#                     user_create_form.email.data,
#                     user_create_form.password.data)
#         db.session.add(user)
#         db.session.commit()

#         msg = Message("Registro novo", sender=app.config["MAIL_USERNAME"], recipients=["72fcosta@gmail.com"])
#         msg.html = render_template("email.html", username=user.username)
#         mail.send(msg)

#     return render_template("user-create.html", form=user_create_form)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     login_form = LoginForm(request.form)
#     if request.method == "POST" and login_form.validate():
#         username = login_form.username.data
#         password = login_form.password.data

#         user = User.query.filter_by(username=username).first()
#         admin = user.admin

#         if user is not None and user.verify_password(password):
#             session["username"] = username
#             session["admin"] = admin
#             return redirect(url_for("index"))
#         else:
#             error_message = "Acesso negado"
#             flash(error_message, "danger")

#         session["username"] = login_form.username.data
#     return render_template("login.html", form=login_form)


# @app.route("/logout")
# def logout():
#     if "username" in session:
#         session.pop("username")
#         session.pop("admin")
#     return redirect(url_for("login"))


@app.route("/ssh-request/<action>", methods=["GET", "POST"])
@app.route("/ssh-request", methods=["GET", "POST"])
def ssh_request(action=""):
    print(action)
    if action == "uptime":
        output = uptime("uptime")
        counter = 1
        lines = {}
        for line in output:
            lines["line{}".format(counter)] = line
            counter += 1
        print(json.dumps(output))
    if action == "ls":
        output = ls("ls")
        counter = 1
        lines = {}
        for line in output:
            lines["line{}".format(counter)] = line
            counter += 1
    return json.dumps(lines)
