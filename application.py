#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def root():
    return redirect("index")
@app.route("/index")
def index():
    conn = sqlite3.connect("zl.db")
    cursor = conn.cursor()
    results = list(cursor.execute("select * from zl"))
    conn.close()
    return render_template("index.html", results=results)

@app.route("/hello/")

def hello():
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    results = list(cursor.execute("select * from list"))
    conn.close()
    return render_template("hello.html", results=results)



