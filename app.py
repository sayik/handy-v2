# This module creates a Flask application.

# It imports the Flask class from the flask module and creates an instance of it. The instance is
# named `app` and is used to define the routes and views of the application.
# Usage:
# - To start the application, run this file using `python app.py`.

from flask import Flask, render_template, jsonify

app = Flask(__name__)

HEROS = [{  
    'id': 1, 'title': 'Triumph Corner',
    'location' : 'to be set', 'cost' : '1000 per/Hr'},
    {'id': 2, 'title': 'Skyline Terrace',  
    'location' : 'New York', 'cost' : '1200 per/Hr'},    
    {'id': 3, 'title': 'Ocean View',
    'location' : 'Los Angeles', 'cost' : '1500 per/Hr'}, 
    {'id': 4, 'title': 'Mountain Retreat',
    'location' : 'Aspen', 'cost' : '2000 per/Hr'},
    {'id': 5, 'title': 'Sunset Oasis',        
    'location' : 'Miami'}
]


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/heros")
def heros():
    return render_template("heros.html", Heros=HEROS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(HEROS)

# needs to do login

# 

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

