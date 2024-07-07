from flask import Flask, url_for

app = Flask(__name__, instance_relative_config=True)
from flaskr import routes