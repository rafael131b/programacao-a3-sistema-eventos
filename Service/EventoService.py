# Services/EventoService.py
from DB.BancoDeDados import BancoDeDados
from Model.EventoModel import EventoModel

banco = BancoDeDados()

# Cria as tabelas no banco de dados
banco.criar_tabelas()
class EventoService:
    def __init__(self):
        self.eventos = []

    def criar_evento(self, idEvento, nomeEvento, endereco, categoria, horario, descricao):
        evento = EventoModel(id=idEvento, nome=nomeEvento, endereco=endereco, categoria=categoria, horario=horario, descricao=descricao)
        banco.inserir_evento(nomeEvento,endereco,categoria,horario,descricao)
        self.eventos.append(evento)
        print(f"Evento {nomeEvento} criado com sucesso.")

    def obter_todos_eventos(self):
        banco.imprimir_eventos()
        return self.eventos

    def obter_evento_por_id(self, idInput):
        for evento in self.eventos:
            if evento.id == idInput:
                return evento
        print(f"Evento com ID {idInput} não encontrado.")
        return None

    def adicionar_usuario_ao_evento(self, usuario, id_evento):
        evento = self.obter_evento_por_id(id_evento)

        if evento and evento not in usuario.eventos_associados:
            usuario.adicionar_evento_associado(evento)
            evento.adicionar_usuario_associado(usuario)
            print("Usuário adicionado ao evento.")
        else:
            print("Evento não válido ou já associado ao usuário.")
