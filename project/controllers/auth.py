# -*- coding: utf-8 -*-
from project import app
from bottle import template, request
from project.utils.cpf_check import CPF
import csv
import sys

import sqlite3

VALIDO = "113.451.253-80"
INVALIDO = "31354110274"

valido = CPF(VALIDO)
invalido = CPF(INVALIDO)

assert valido.isValid()
assert invalido.isValid()

@app.route('/users')
def show_users():
    db = sqlite3.connect('users.db')
    c = db.cursor()
    c.execute("SELECT email,password,cpf FROM users")
    data = c.fetchall()
    c.close()
    output = template('show_users', rows=data)
    return output

@app.route('/', method='GET')
def index():
    return template('index', message='')


@app.route('/login', method=['POST'])
def login():
    db = sqlite3.connect('users.db')
    c = db.cursor()
    nome = request.POST['nome']
    email = request.POST['email']
    cpf = request.POST['cpf']
    valido = CPF(cpf)

    if valido.isValid():
        f = open('users.csv', 'wt')
        try:
            writer = csv.writer(f)
            writer.writerow( ('nome', 'cpf', 'email') )
            writer.writerow(nome, email, cpf)
        finally:
            f.close()

        print open('users.csv', 'rt').read()

        # c.execute('INSERT INTO users (nome, email, cpf) VALUES (?,?,?)',(nome, email, cpf))
        # db.commit()
    else:
        return template('index', message='CPF INVÁLIDO')
    return template('index', message='')
