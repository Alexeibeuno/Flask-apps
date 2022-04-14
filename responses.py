import flask
from flask import Flask
app = Flask(__name__)
from flask import request

#Example1
@app.route('/')
def index():
    return '<h1>Bad request</h1>', 400

#The below example creates a response object and sets a cookie in it
from flask import make_response
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

#redirect
from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')


#abort function
from flask import abort
@app.route('/user/<id>')
def get_user(id):
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' %user.name