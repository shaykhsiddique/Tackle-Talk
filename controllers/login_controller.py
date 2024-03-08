
from flask import render_template

def loginView():
    data = {
        'title': 'Tackle Talk',
        'content': 'Hello, this is a Flask app with Jinja templates!'
    }
    return render_template('login.html', data=data)