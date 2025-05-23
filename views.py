from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, bd
from models import Jogos, Usuarios
# ROTAS #


@app.route('/')
def index():
    listaJogos = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo="Lista de Jogos", jogos=listaJogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    name = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogos.query.filter_by(nome=name).first()
    if jogo:
        flash('Jogo ja existe no cadastro!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=name, categoria=categoria, console=console)
    bd.session.add(novo_jogo)
    bd.session.commit()
    flash('Jogo inserido com sucesso!')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(
        nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'logado com sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)  # <--- link quebrado
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect(url_for('index'))
    else:
        session['usuario_logado'] = None
        flash('usuário deslogado com sucesso!')
        return redirect(url_for('index'))
