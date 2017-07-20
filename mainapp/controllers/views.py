#! /usr/bin/python3
# -*- coding: utf-8 -*-
from mainapp import app
from mainapp.controllers.ssh import Inside
from flask import render_template
from flask import request
import json


@app.errorhandler(404)
def page_not_found(e):
    return render_template("page-404.html"), 404


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/ssh-request/list-onts", methods=["GET", "POST"])
def list_onts():
    inside = Inside()
    status_onts = inside.status_onts()
    print("list_onts() => {}".format(status_onts))
    return json.dumps(status_onts)


@app.route("/ssh-request/authorize", methods=["GET", "POST"])
def authorize():
    inside = Inside()
    F = request.args.get("F", "Err")
    S = request.args.get("S", "Err")
    P = request.args.get("P", "Err")
    next_ont_id = inside.next_ont_id(F, S, P)
    return json.dumps(next_ont_id)
