# -*- coding: utf-8 -*-
from project import app
from bottle import template, request
from project.utils.cpf_check import CPF

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
    email = request.POST['email']
    password = request.POST['password']
    cpf = request.POST['cpf']
    valido = CPF(cpf)

    if valido.isValid():
        c.execute('INSERT INTO users (email,password,cpf) VALUES (?,?,?)',(email,password,cpf))
        db.commit()

    return template('index', message='')
