import os

from cs50 import SQL
import json
from helper import lookup, bss_code
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

query = "hey"

@app.route("/", methods = ["GET", "POST"])
def index():
    global query
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        query = request.form.get("query")
        if query == "":
            query = "fhdsfkjsadhfbn,gjvasdbj,"
        return redirect("/search")

@app.route("/search")
def search():
    rawjson = json.loads(lookup(query).text)
    if rawjson["totalItems"] == 0:
        return render_template("search.html", title = "Sorry we can't find anything")
    totalItems = rawjson["totalItems"]
    books_list = []
    for i in rawjson["items"]:
        isbn = int(i["volumeInfo"]["industryIdentifiers"][0]["identifier"])
        title = i["volumeInfo"]["title"]
        author = i["volumeInfo"]["authors"][0]
        try:
            description = i["volumeInfo"]["description"]
        except:
            description = "No description"
        try:
            img = i["volumeInfo"]["imageLinks"]["thumbnail"]
        except:
            img = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fonlinebookclub.org%2Freviews%2F&psig=AOvVaw1SptIdLhwE9PtdoVV2dpBX&ust=1705603230485000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJiItaiJ5YMDFQAAAAAdAAAAABAI"
        try:
            bss = bss_code(i["volumeInfo"]["categories"][0])        
        except:
            bss = bss_code("UKNOWN")
        check = db.execute("SELECT * FROM books WHERE isbn = ?", int(i["volumeInfo"]["industryIdentifiers"][0]["identifier"]))
        if len(check) == 0:
            db.execute("INSERT INTO books (isbn, title, author, description, img, bss) VALUES (?, ?, ?, ?, ?, ?)",
                isbn,
                title,
                author,
                description,
                img,
                bss
                )
        tmp = {"isbn": isbn, "bss": bss, "title": title, "author": author, "description": description, "img_link": img}
        books_list.append(tmp)
    rawjson = rawjson["items"][0]["volumeInfo"]
    return render_template("search.html",
                           results = totalItems,
                           query = books_list
    )
    # return render_template("search.html",
    #                        results = totalItems,
    #                        isbn = int(rawjson["industryIdentifiers"][0]["identifier"]),
    #                        bss = db.execute("SELECT bss FROM books WHERE isbn = ?", int(rawjson["industryIdentifiers"][0]["identifier"]))[0]["bss"],
    #                        title = rawjson["title"],
    #                        author = rawjson["authors"][0],
    #                        description = rawjson["description"],
    #                        img_link = rawjson["imageLinks"]["thumbnail"]
    # )
