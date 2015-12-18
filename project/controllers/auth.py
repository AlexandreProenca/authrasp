# -*- coding: utf-8 -*-
from project import app
from bottle import template, request, redirect
from project.utils.cpf_check import CPF
import csv
from project.sinc.sinc import Sinc
import ConfigParser
import time
import logging
import os

# Path to log file
dir_script = os.path.dirname(os.path.abspath(__file__))
auth = dir_script+'/auth-rasp2.log'

# Log, formater and file
logging.basicConfig(format='[%(asctime)s] - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename=auth)


config = ConfigParser.RawConfigParser()
config.read('config.txt')

debug = config.get('config', 'DEBUG')
sh_start = config.get('config', 'SH_START')
sh_stop = config.get('config', 'SH_STOP')
url_redirect = config.get('config', 'URL_REDIRECT')
tempo = config.get('config', 'TEMPO_CONEXAO')

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
    f = open('log.txt', 'a')
    f.write("Date: "+str(time.clock())+" Info: "+str(request.json))
    if debug:
        logging.info("LOGIN Nome: [%s] | Email: [%s] | CPF: [%s]" % (nome, email, cpf))

    if valido.isValid():

        try:
            Sinc.insert({'delta': 0, 'info': 'imediato', 'path': sh_start+" "+client_ip})
            Sinc.insert({'delta': tempo, 'info': 'sh de 30 segundos', 'path': sh_stop+" "+client_ip})
        except Exception as e:
            if debug:
                logging.ERROR("ERROR WITH SINC %s" % str(e))

        f = open('users.csv', 'a')
        try:
            writer = csv.writer(f)
            writer.writerow((nome, email, cpf, client_ip))
        except:
            if debug:
                logging.error("Não foi possivel escrever no arquivo")
        finally:
            f.close()

    else:
        return template('index', message='CPF INVÁLIDO')

    if debug:
        logging.info("REDIRECIONADO CLIENT: [%s] para [%s]" % (str(client_ip),url_redirect))

    return redirect(url_redirect, code=302)

