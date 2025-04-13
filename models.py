from jogoteca import bd
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
