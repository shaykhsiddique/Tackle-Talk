from flask import render_template
from mlmodels.extractpopularplayers import pridectplayers  # Adjust the import path based on your project structure

def home():
    data = {
        'title': 'Tackle Talk',
        'content': 'Hello, this is a Flask app with Jinja templates!',
        'prediction': pridectplayers()  # Assuming predict is a function in mlmodel module
    }
    return render_template('home.html', data=data)