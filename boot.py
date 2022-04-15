import flask
from flask import Flask
import flask_bootstrap
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
