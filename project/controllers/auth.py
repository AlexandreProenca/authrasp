# -*- coding: utf-8 -*-
from project import app
from bottle import template, request, redirect
from project.utils.cpf_check import CPF
import csv
from project.sinc.sinc import Sinc
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.txt')

sh_start = config.get('config', 'SH_START')
sh_stop = config.get('config', 'SH_STOP')
url_redirect = config.get('config', 'URL_REDIRECT')

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

    if valido.isValid():
        Sinc.insert({'delta': 0, 'info': 'imediato', 'path': sh_start})
        Sinc.insert({'delta': 30, 'info': 'sh de 30 segundos', 'path': sh_stop})

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
    return redirect(url_redirect, code=302)

