from main import app
from flask import render_template, request, redirect
from flask import request

@app.route("/")
def homepage():
    return render_template('index.html')

# @app.route("/soma", methods=['POST'])
# def soma():
#     try:
#         num1 = request.form.get('num1')
#         num2 = request.form.get('num2')
#         print(num1 + num2)
#
#         num1 += int(num1)
#         num2 += int(num2)
#         return num1 + num2
#     except:
#         return "erro"
