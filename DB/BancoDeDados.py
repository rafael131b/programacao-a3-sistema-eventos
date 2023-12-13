class BancoDeDados:
    def __init__(self, nome_do_arquivo='dados.txt'):
        self.nome_do_arquivo = nome_do_arquivo

    def criar_tabelas(self):

        pass

    def inserir_usuario(self, nome, email, cpf):
        with open(self.nome_do_arquivo, 'a') as arquivo:
            arquivo.write(f'Usuario: Nome: {nome}, Email: {email}, CPF: {cpf}\n')


    def inserir_evento(self, nome_evento, endereco, categoria, horario, descricao):
        with open(self.nome_do_arquivo, 'a') as arquivo:
            arquivo.write(f'Evento: Nome: {nome_evento}, Endereço: {endereco}, Categoria: {categoria},'
                          f' Horário: {horario}, Descrição: {descricao}\n')

    def imprimir_usuarios(self):
        with open(self.nome_do_arquivo, 'r') as arquivo:
            print('\nLista de Usuários:')
            for linha in arquivo:
                if linha.startswith('Usuario:'):
                    print(linha.strip())

    def imprimir_eventos(self):
        with open(self.nome_do_arquivo, 'r') as arquivo:
            print('\nLista de Eventos:')
            for linha in arquivo:
                if linha.startswith('Evento:'):
                    print(linha.strip())


