#! /usr/bin/python3
# -*- coding: utf-8 -*-
from mainapp import app
from mainapp.controllers.ssh import StatusOnts
from flask import render_template
import json


@app.errorhandler(404)
def page_not_found(e):
    return render_template("page-404.html"), 404


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/ssh-request/list-onts", methods=["GET", "POST"])
def ssh_request():
    status_onts = StatusOnts()
    # status_onts_in_json = status_onts.in_json()
    status_onts_in_json = status_onts.in_json(["enable", "config", "scroll 512", "display ont autofind all"])
    print(status_onts_in_json)
    return json.dumps(status_onts_in_json)
