#! /usr/bin/python3
# -*- coding: utf-8 -*-
from mainapp import app
from mainapp import db

from mainapp.models.tables import User
from mainapp.models.tables import Olt

from mainapp.controllers.forms import LoginForm
from mainapp.controllers.forms import UserCreateForm
from mainapp.controllers.forms import UserReadForm
from mainapp.controllers.ssh import Inside

from flask import render_template
from flask import request
from flask import flash
from flask import session
from flask import url_for
from flask import redirect

import json


@app.before_request
def before_request():
    user_pages = ["index", "ssh_request"]
    admin_pages = ["admin", "user_create", "user_edit", "user_delete"]
    if "username" not in session and request.endpoint in user_pages:
        return redirect(url_for("login"))
    elif "username" in session and request.endpoint in ["login"]:
        return redirect(url_for("index"))
    elif "admin" not in session and request.endpoint in admin_pages:
        return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("page-404.html"), 404


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(request.form)
    if request.method == "POST" and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            admin = user.admin
            session["username"] = username
            session["admin"] = admin
            print(user)
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha inválido!", "danger")
    return render_template("page-login.html", login_form=login_form)


@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        session.pop("admin")
    return redirect(url_for("login"))


@app.route("/user-create", methods=["GET", "POST"])
def user_create():
    user_create_form = UserCreateForm(request.form)
    if request.method == "POST" and user_create_form.validate():
        user = User(user_create_form.username.data,
                    user_create_form.name.data,
                    user_create_form.cpf.data,
                    user_create_form.company.data,
                    user_create_form.cnpj.data,
                    user_create_form.email.data,
                    user_create_form.password.data
                    )
        db.session.add(user)
        db.session.commit()
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for("user_create"))

    return render_template("page-user-create.html", form=user_create_form)


@app.route("/user-read", methods=["GET", "POST"])
def user_read():
    user_read_form = UserReadForm(request.form)
    if request.method == "POST" and user_read_form.validate():
        username = user_read_form.username.data
        return redirect(url_for("index"))

    return render_template("page-user-read.html", form=user_read_form)


@app.route("/user-list", methods=["GET", "POST"])
def user_list():
    user_read_form = UserReadForm(request.form)
    if request.method == "POST" and user_read_form.validate():
        username = user_read_form.username.data
        return redirect(url_for("index"))

    return render_template("page-user-list.html", form=user_read_form)


# @app.route("/olt-create", methods=["GET", "POST"])
# def olt_create():
#     user_create_form = UserCreateForm(request.form)
#     if request.method == "POST" and user_create_form.validate():
#         user = User(user_create_form.username.data,
#                     user_create_form.name.data,
#                     user_create_form.cpf.data,
#                     user_create_form.company.data,
#                     user_create_form.cnpj.data,
#                     user_create_form.email.data,
#                     user_create_form.password.data
#                     )
#         db.session.add(user)
#         db.session.commit()
#         flash("Usuário cadastrado com sucesso!", "success")
#         return redirect(url_for("user_create"))

#     return render_template("page-user-create.html", form=user_create_form)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    pass
    return render_template("page-admin.html")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("page-control.html")


@app.route("/ssh-request/list-onts", methods=["GET", "POST"])
def list_onts():
    inside = Inside()
    status_onts = inside.status_onts()
    print("list_onts() => {}".format(status_onts))
    return json.dumps(status_onts)


@app.route("/ssh-request/authorize", methods=["GET", "POST"])
def authorize():
    inside = Inside()
    sn = request.args.get("sn", "Err")
    f = request.args.get("f", "Err")
    s = request.args.get("s", "Err")
    p = request.args.get("p", "Err")
    vendorId = request.args.get("vendorId", "Err")
    description = request.args.get("description", "Err")
    description = description.strip()
    if len(description) < 1:
        description = "sem_desc"
    if len(description) > 4:
        description = description[:10]
    vlan = request.args.get("vlan", "Err")
    vlan = vlan.strip()
    if len(vlan) < 1:
        vlan = "100"
    if len(vlan) > 4:
        vlan = vlan[:4]
    scriptType = request.args.get("scriptType", "Err")
    gemPort = request.args.get("gemPort", "Err")
    authorize_ont = inside.authorize_ont(sn, f, s, p, vendorId, description, vlan, scriptType, gemPort)
    return json.dumps(authorize_ont)
