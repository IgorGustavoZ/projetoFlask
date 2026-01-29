from operator import countOf

from werkzeug.utils import secure_filename

from main import app
from flask import render_template, request, redirect, jsonify

import time
import os
import win32api

UPLOAD_FOLDER = r"uploads" #definindo a pasta onde será salvo as imagens
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def homepage():
    return render_template('index.html')

#exclui todos os arquivos de 'uploads'
def excludeUpload(arquivos, caminho):
    for arquivo in arquivos:
        os.remove(os.path.join(caminho, arquivo))

#imprime os arquivos do diretório uploads.
@app.route("/upload", methods=['POST'])
def upload():
    arquivos = os.listdir(UPLOAD_FOLDER)

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
        print("Ocorreu um erro de impressão : ", e)
        return "Erro na impressão !"

num = 0
#Salvamento automático em uploads, chamado toda vez que o input file muda-se seu valor.
@app.route("/save", methods=['POST'])
def save():
    try:
        num = os.listdir(UPLOAD_FOLDER).__len__() + 1
        # -pega a imagem
        file = request.files.get('arq') # no get () o parametro usado é o atributo name do input file.
        # -salva um nome seguro, sem riscos de segurança
        file.filename = secure_filename(str(num) + "." + file.filename.rsplit('.', 1)[1].lower())
        # -salva na pasta uploads com o seu nome
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        file.save(os.path.join("static\img", file.filename))

        return redirect("/")
    except Exception as e:
        print("Erro na instalação das imagens : ", e)
        return redirect("Erro na instalação das imagens !")


