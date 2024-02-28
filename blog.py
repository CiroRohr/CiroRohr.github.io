from flask import Blueprint, Flask, render_template
from markupsafe import escape
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    
    list=os.listdir("./posts")
    posts = []
    for i, l in enumerate(list):
        file = f"./posts/{l}"
        with open(file, 'r') as f:
            posts.append(json.load(f))

    return render_template('index.html', posts=posts)

@app.route('/post/<path:postname>')
def post(postname):
    with open(f"./posts/{postname}.json", 'r') as f:
        data = json.load(f)

    return render_template('posts.html', data=data)
