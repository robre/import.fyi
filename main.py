#!/usr/bin/env python3
# (c) @r0bre (mail[ät]r0b.re)
# Created: 05/06/2021 

from flask import Flask, jsonify, render_template, url_for
import yaml
import glob
from fuzzywuzzy import process

import logzero
from logzero import logger as log

app = Flask(__name__)

module_yamls = glob.glob("modules/*.yaml")
modules = {}
for f in module_yamls:
    with open(f,"r") as s:
        try:
            modname = f.split(".yaml")[0].split("/")[-1]
            modules[modname] = yaml.safe_load(s)
            log.info(f"{modname} loaded into db")
        except yaml.YAMLError as e:
            log.error(f"Yaml Exeption when reading {f}: {e}")

categories = ["http-server", "http-client", "serialization", "filesystem", "logging", "search", "hacking"]

print(modules)

@app.route("/")
def hello_world():
    return render_template("home.html", categories=categories)

@app.route("/module/<modulename>")
def module(modulename):
    return render_template("module.html", module=modules[modulename])


@app.route("/submit/")
def submit():
    return render_template("submit.html")

@app.route("/error/")
def error():
    return render_template("error.html")

@app.route("/search/<searchterm>")
def search(searchterm):
    results = list(filter(lambda s: s[1]>30,process.extract(searchterm, modules, limit=10)))
    log.info(results)
    return render_template("search.html", searchterm=searchterm, results=results)

@app.route("/browse/")
def browse():
    return render_template("browse.html", categories=categories, modules=modules)




# @app.route("/api/module/<modulename>")
# def api_module(modulename):
#     return render_template("home.html")

# @app.route("/api/category/<category>")
# def api_category(category):
#     return render_template("home.html")

# @app.route("/api/tags/<tags>")
# def api_tags(tags):
#     return render_template("home.html")

