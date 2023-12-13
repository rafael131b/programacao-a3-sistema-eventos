from Service.UsuarioService import UsuarioService
from Service.EventoService import EventoService

def main():


    usuario_service = UsuarioService()
    evento_service = EventoService()

    while True:
        print("\nOpções:")
        print("1. Criar Usuário")
        print("2. Criar Evento")
        print("3. Obter Todos os Eventos")
        print("4. Obter Todos os Usuários")
        print("5. Adicionar Usuário a um Evento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario(usuario_service)
        elif opcao == "2":
            criar_evento(evento_service)
        elif opcao == "3":
            obter_todos_eventos(evento_service)
        elif opcao == "4":
            obter_todos_usuarios(usuario_service)
        elif opcao == "5":
            adicionar_usuario_a_evento(usuario_service, evento_service)
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def criar_usuario(usuario_service):
    idUsuario = input("Digite o ID do usuário: ")
    nomeUsuario = input("Digite o Nome do Usuário: ")
    cpfUsuario = input("Digite o CPF do Usuário: ")
    emailUsuario = input("Digite o Email do Usuário: ")
    senhaUsuario = input("Digite a Senha do Usuário: ")


    usuario_service.criar_usuario(nomeUsuario, cpfUsuario, emailUsuario, senhaUsuario)


def criar_evento(evento_service):
    idEvento = input("Digite o ID do evento: ")
    nomeEvento = input("Digite o Nome do Evento: ")
    endereco = input("Digite o Endereço do Evento: ")
    categoria = input("Digite a Categoria do Evento: ")
    horario = input("Digite o Horário do Evento: ")
    descricao = input("Digite a Descrição do Evento: ")

    evento_service.criar_evento(idEvento, nomeEvento, endereco, categoria, horario, descricao)

def obter_todos_eventos(evento_service):
    eventos = evento_service.obter_todos_eventos()

    if eventos:
        print("\nLista de Eventos:")
        for evento in eventos:
            print(evento)
    else:
        print("Não há eventos disponíveis.")

def obter_todos_usuarios(usuario_service):
    usuarios = usuario_service.obter_todos_usuarios()

    if usuarios:
        print("\nLista de Usuários:")
        for usuario in usuarios:
            print(usuario)
    else:
        print("Não há usuários disponíveis.")

def adicionar_usuario_a_evento(usuario_service, evento_service):
    cpf_usuario = input("Digite o CPF do usuário: ")
    usuario = usuario_service.obter_usuario_por_cpf(cpf_usuario)

    if usuario:
        id_evento = input("Digite o ID do evento: ")
        evento_service.adicionar_usuario_ao_evento(usuario, id_evento)
    else:
        print(f"Usuário com CPF {cpf_usuario} não encontrado.")
if __name__ == "__main__":
    main()
