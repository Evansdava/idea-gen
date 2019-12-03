from flask import Flask, render_template
from random import choice
# from pattern.text.en import pluralize


app = Flask(__name__)


@app.route("/")
def index():
    """Display the home page for generating ideas"""
    idea = ""
    with open('words/base.txt') as f:
        bases = f.readlines()
    with open('words/noun.txt') as f:
        nouns = f.readlines()

    base = choice(bases)
    noun = choice(nouns).strip()
    idea = f"{base} but for {noun}"
    return render_template('index.html', idea=idea)


@app.route("/possibilities")
def word_list():
    """Display an editable list of words that can appear"""
    words = []
    with open('words/words.txt') as f:
        words = f.readlines()
    return render_template('word_list.html', words=words)


@app.route("/saved")
def saved():
    """Display the words saved by the user"""
    ideas = [
        "here's an idea that was saved",
        "here is another",
        "here is one that's really long but not too long probably",
        "more ideas go here and below"
        ]
    return render_template('saved.html', ideas=ideas)
