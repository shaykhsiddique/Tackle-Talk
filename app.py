# @author: Shaykh Siddique
# @email: shaykhsiddiqee@gmail.com
# @copyright: all rights are reserved by author

from flask import Flask
from controllers.home_controller import home

app = Flask(__name__)

# Use the home function as a route
@app.route('/')
def index():
    return home()

if __name__ == '__main__':
    # Run the app on port 5001 (you can change this to any available port)
    app.run(host='0.0.0.0', debug=True, port=5002)