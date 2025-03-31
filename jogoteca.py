from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'alura'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='admin',
        servidor='localhost',
        database='jogoteca'
)
bd = SQLAlchemy(app)

# uma classe para cada tabela (POO)


class Jogos(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    nome = bd.Column(bd.String(50), nullable=False)
    categoria = bd.Column(bd.String(40), nullable=False)
    console = bd.Column(bd.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(bd.Model):
    nickname = bd.Column(bd.String(8), primary_key=True)
    nome = bd.Column(bd.String(20), nullable=False)
    senha = bd.Column(bd.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

##################################################################################


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("Skyrim", "RPG", "PC")
jogo2 = Jogo("Fifa", "futebol", "Xbox")
jogo3 = Jogo("GTA", "RPG", "PS2")
listaJogos = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    # listaJogos = ['Skyrim', 'Fifa', 'GTA']
    return render_template('lista.html', titulo="Lista de Jogos", jogos=listaJogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    listaJogos.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        proxima_page = request.form['proxima']
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/{}'.format(proxima_page))
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


app.run(debug=True)
