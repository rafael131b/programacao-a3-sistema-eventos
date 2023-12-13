# Models/UsuarioModel.py

class UsuarioModel:
    def __init__(self, id, nome, cpf, email, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.eventos_associados = []

    def adicionar_evento_associado(self, evento):
        self.eventos_associados.append(evento)

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}"
