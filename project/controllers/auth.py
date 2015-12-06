# -*- coding: utf-8 -*-
from project import app
from bottle import template, request
import sqlite3

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
    c.execute('INSERT INTO users (email,password,cpf) VALUES (?,?,?)',(email,password,cpf))
    db.commit()

    return template('index', message='')
