import flask
from flask import Flask
app = Flask(__name__)
from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' %user_agent