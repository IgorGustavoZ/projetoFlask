from flask import Flask
app = Flask(__name__)

from views import *

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/soma")
# def soma():
#     return "2"

if __name__ == "__main__": app.run()