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


@app.route("/control-panel", methods=["GET", "POST"])
def control_panel():
    return render_template("control-panel.html")


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
