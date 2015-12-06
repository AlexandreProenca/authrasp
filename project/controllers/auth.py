# -*- coding: utf-8 -*-
import time
from project import app
from bottle import template, request, redirect
from project.utils.cpf_check import CPF
import csv
from subprocess import call

@app.route('/', method='GET')
def index():
    return template('index', message='')


@app.route('/login', method=['POST'])
def login():
    nome = request.POST['nome']
    email = request.POST['email']
    cpf = request.POST['cpf']
    valido = CPF(cpf)
    client_ip = request.environ.get('REMOTE_ADDR')
    print ['Your IP is: {}\n'.format(client_ip)]

    if valido.isValid():
        #call("start.sh", shell=True)
        #call_stop()

        f = open('users.csv', 'a')
        try:
            writer = csv.writer(f)
            writer.writerow((nome, email, cpf, client_ip))

        except:
            print("Não foi possivel escrever no arquivo")
        finally:
            f.close()

    else:
        return template('index', message='CPF INVÁLIDO')
    return template('index', message=' cadastro oks')



def call_stop():
    time.sleep(30)
    call("stop.sh")
    redirect("http://www.google.com", code=302)
