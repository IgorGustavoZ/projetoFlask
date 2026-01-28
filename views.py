from werkzeug.utils import secure_filename

from main import app
from flask import render_template, request, redirect, jsonify

import time
import os
import win32api

UPLOAD_FOLDER = r"uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def homepage():
    return render_template('index.html')

def excludeUpload(arquivos, caminho):
    for arquivo in arquivos:
        os.remove(os.path.join(caminho, arquivo))
@app.route("/upload", methods=['POST'])
def upload():
    arquivos = os.listdir(r"C:\Users\V12 Informatica\Desktop\projetoFlask\uploads")

    try:
        if(arquivos != None):

            for arquivo in arquivos:
                caminho = os.path.join(UPLOAD_FOLDER, arquivo)
                win32api.ShellExecute(
                    0, "print",
                    caminho,
                    None,
                    ".",
                    0)
            time.sleep(10)
            excludeUpload(arquivos, UPLOAD_FOLDER)
        return redirect('/')
    except Exception as e:
        print("Ocorreu um erro de impressão: ", e)
        return "Erro na impressão !"
@app.route("/save", methods=['POST'])
def save():
    try:
        file = request.files['arq']
        file.filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect("/")
    except Exception as e:
        print("Erro na instalação das imagens", e)
        return redirect("Erro na instalação das imagens !")


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
