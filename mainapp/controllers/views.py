#! /usr/bin/python3
# -*- coding: utf-8 -*-
from mainapp import app
from mainapp.controllers.ssh import StatusOnts
from mainapp.controllers.ssh import NextOntId
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
    status_onts = StatusOnts()
    status_onts_filtered = status_onts.filtered()
    # status_onts_filtered = status_onts.filtered(["enable", "config", "scroll 512", "display ont autofind all"])
    return json.dumps(status_onts_filtered)


@app.route("/ssh-request/authorize", methods=["GET", "POST"])
def authorize():
    F = request.args.get("F", "Err")
    S = request.args.get("S", "Err")
    P = request.args.get("P", "Err")
    next_ont_id = NextOntId(F, S, P)
    return json.dumps(next_ont_id)
