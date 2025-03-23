from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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
    return render_template('novo.html', titulo="Novo Cadastro")


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    listaJogos.append(jogo)
    return redirect('/')


app.run(debug=True)
