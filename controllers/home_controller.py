
from flask import render_template

def home():
    data = {
        'title': 'Tackle Talk',
        'content': 'Hello, this is a Flask app with Jinja templates!'
    }
    return render_template('index.html', data=data)