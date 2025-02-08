from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
import json

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///wordsapp.db")

def reshape_and_reshuffle(query_result):
    reshuffled_data = []

    for item in query_result:
        reshuffled_data.append({"id": item["id"], "lang": item["english"]})
        reshuffled_data.append({"id": item["id"], "lang": item["dutch"]})

    random.shuffle(reshuffled_data)
    return reshuffled_data

@app.route("/")
def index():
    """Select library, redirect user to match page"""
    if request.method == "GET":
        libraries = db.execute("SELECT DISTINCT library FROM words;")
        return render_template("index.html",libraries=libraries)

@app.route("/game")
def game():
    """Make a page with word pairs"""
    library = request.args.get('library', 'animals')

    if request.method == "GET":
        words = db.execute("SELECT * FROM words WHERE library = ?;",library)
        words_reshuffled = reshape_and_reshuffle(words)
        wordsamount = len(words)
        return render_template("game.html",words_reshuffled=words_reshuffled ,wordsamount=wordsamount)

@app.route("/api/words")
def words():
    """Get words from library"""
    if request.method == "GET":
        return db.execute("SELECT * FROM words;")


if __name__ == "__main__":
    app.run(debug=True)
