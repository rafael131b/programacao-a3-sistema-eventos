# Models/EventoModel.py
from Model.UsuarioModel import UsuarioModel

class EventoModel:
    def __init__(self, id, nome, endereco, categoria, horario, descricao):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.categoria = categoria
        self.horario = horario
        self.descricao = descricao
        self.listaUsuarios = []

    def adicionar_usuario_associado(self, usuario):
        self.listaUsuarios.append(usuario)

    def __str__(self):
        usuarios_str = ", ".join(map(str, self.listaUsuarios))+ "]"
        return f"ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}, Categoria: {self.categoria}, Horário: {self.horario}, Descrição: {self.descricao}, Evento:  [ {usuarios_str}, "
