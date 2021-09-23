from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import Logins, Usuario
from dao import LoginsDao, UsuarioDao
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key ='vrraaau'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "password"
app.config['MYSQL_DB'] = "emails"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

logins_dao = LoginsDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    lista = logins_dao.listar()
    return render_template('lista.html', titulo='Logins', Logins=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Primeiramente faca seu login')
        return redirect(url_for('index'))
    return render_template('novo.html', titulo='Novo Login')


@app.route('/criar', methods =['POST'])
def criar() :
    nome = request.form['nome']
    email = request.form['email']
    senha = request. form['senha']
    login = Logins(nome, email, senha)
    logins_dao.salvar(login) 
    
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods =['POST'])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.password == request.form['password']:
            session['usuario_logado'] =usuario.id
            flash('Ola '+ usuario.usuario + '. Logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)    

    else:
        flash('Erro no login')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado!')
    return redirect(url_for('index'))




app.run(debug =True)