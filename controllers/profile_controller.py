
from flask import render_template

def profile(playername):
    data = {
        'title': 'Tackle Talk',
        'content': 'Hello, this is a Flask app with Jinja templates!',
        'PlayerName': playername
    }
    return render_template('playerprofile.html', data=data)