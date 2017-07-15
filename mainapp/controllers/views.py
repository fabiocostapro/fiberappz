#! /usr/bin/python3
# -*- coding: utf-8 -*-
from mainapp import app
from mainapp.controllers.ssh import enable
from flask import render_template
import json


@app.errorhandler(404)
def page_not_found(e):
    return render_template("page-404.html"), 404


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/ssh-request/<action>", methods=["GET", "POST"])
@app.route("/ssh-request", methods=["GET", "POST"])
def ssh_request(action=""):
    print(action)
    lines = {}
    if action == "enable":
        output = enable("enable")
        counter = 1
        for line in output:
            lines["line{}".format(counter)] = line
            counter += 1
        print(json.dumps(output))
    return json.dumps(lines)
