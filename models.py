class Logins:
    def __init__(self, nome, email, senha, id= None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha


class Usuario:
    def __init__(self, id, usuario, password):
        self.id= id
        self.usuario = usuario
        self.password = password