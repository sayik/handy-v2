# This module creates a Flask application.

# It imports the Flask class from the flask module and creates an instance of it. The instance is
# named `app` and is used to define the routes and views of the application.
# Usage:
# - To start the application, run this file using `python app.py`.

from flask import Flask, render_template, jsonify
from database import load_talents_db


app = Flask(__name__)


# Render homepage
@app.route('/')
def index():
    return render_template("index.html")

# Render talents
@app.route("/heros")
def heros():
    talents = load_talents_db()
    return render_template("heros.html", Heros=talents)

# json data
@app.route("/api/jobs")
def list_jobs():
    talents = load_talents_db()
    return jsonify(talents)




# needs to do login

# 

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

