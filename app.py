import os

from cs50 import SQL
import json
from helper import lookup
import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
Session(app)

db = SQL("sqlite:///bss.db")

query = ""

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    query = request.form.get("query")
    print(query)
    return redirect("/search")

@app.route("/search")
def search():
    return render_template("search.html", query = query)