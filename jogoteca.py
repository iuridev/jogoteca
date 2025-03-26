from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'alura'


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
    ##listaJogos = ['Skyrim', 'Fifa', 'GTA']
    return render_template('lista.html', titulo="Lista de Jogos", jogos=listaJogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo="Novo Cadastro")


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    listaJogos.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        proxima_page = request.form['proxima']
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/{}'.format(proxima_page))
    else:
        flash('Usuário não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    else:
        session['usuario_logado'] = None
        flash('usuário deslogado com sucesso!')
        return redirect('/')

app.run(debug=True)
