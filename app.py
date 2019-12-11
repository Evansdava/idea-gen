import requests
import os
import json
from flask import Flask, render_template
from random import choice
# from pattern.text.en import pluralize
from dotenv import load_dotenv
load_dotenv()

UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")


app = Flask(__name__)


@app.route("/")
def index():
    """Display the home page for generating ideas"""
    key = UNSPLASH_API_KEY
    idea = ""
    with open('words/base.txt') as f:
        bases = f.readlines()
    with open('words/noun.txt') as f:
        nouns = f.readlines()

    base = choice(bases)
    noun = choice(nouns).strip() + "s"
    idea = f"{base} but for {noun}"

    params = {
        "client_id": key,
        "query": noun
    }

    r = requests.get("https://api.unsplash.com/photos/random", params=params)
    img = json.loads(r.content)

    return render_template('index.html', idea=idea, img=img)


@app.route("/possibilities")
def word_list():
    """Display an editable list of words that can appear"""
    with open('words/noun.txt') as f:
        words = f.readlines()

    with open('words/base.txt') as f:
        bases = f.readlines()

    params = {
        "client_id": UNSPLASH_API_KEY,
        "query": 'possibilities'
    }

    r = requests.get("https://api.unsplash.com/photos/random", params=params)
    img = json.loads(r.content)

    return render_template('word_list.html', words=words, bases=bases, img=img)


@app.route("/saved")
def saved():
    """Display the words saved by the user"""
    ideas = [
        "here's an idea that was saved",
        "here is another",
        "here is one that's really long but not too long probably",
        "more ideas go here and below"
        ]

    params = {
        "client_id": UNSPLASH_API_KEY,
        "query": 'saved'
    }

    r = requests.get("https://api.unsplash.com/photos/random", params=params)
    img = json.loads(r.content)
    return render_template('saved.html', ideas=ideas, img=img)
