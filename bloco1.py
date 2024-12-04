from aluno import Aluno

aluno1 = Aluno(
    nome="João", 
    sobrenome="Silva", 
    nome_user= "joao123",
    endereco="Rua A", 
    email="joao@email.com",
    senha="1234567890",
    medio_superior=True, 
    status= True,
    email_resp="paidojoao@gmail.com",
    registro_academ="Joao4321",
    turma="201-MECA",
    bacharel_ciencias=False,
    bacharel_pedago=False,
    curso="mecatrônica")


def menu_aluno(aluno):
    while True:
        print("\n--- Menu de Opções ---")
        print("1 - Editar Dados")
        print("2 - Listar Dados")
        print("3 - Desativar Aluno")
        print("4 - Reativar Aluno")
        print("5 - Excluir Aluno")
        print("6 - Sair")

        try:
            escolha = int(input("Escolha uma opção: "))
            
            if escolha == 1:  # Editar dados
                print("\n--- Editar Dados ---")
                print("1 - Nome e Sobrenome")
                print("2 - Endereço")
                print("3 - E-mail")
                print("4 - E-mail do Responsável")
                print("5 - Registro Acadêmico")
                print("6 - Segmento")
                print("7 - Turma")
                print("8 - Nome de Usuário")
                print("9 - Senha")
                sub_escolha = int(input("Escolha uma opção: "))

                if sub_escolha == 1:
                    nome = input("Novo nome: ")
                    sobrenome = input("Novo sobrenome: ")
                    aluno.set_nome(nome)
                    aluno.set_sobrenome(sobrenome)
                elif sub_escolha == 2:
                    endereco = input("Novo endereço: ")
                    aluno.set_endereco(endereco)
                elif sub_escolha == 3:
                    email = input("Novo e-mail: ")
                    aluno.set_email(email)
                elif sub_escolha == 4:
                    emailreps = input("Nova e-mail de responsavel: ")
                    aluno.set_email_resp(emailreps)
                elif sub_escolha == 5:
                    regiacade = input("Novo registro acadêmico:")
                    aluno.set_registro_academ(regiacade)
                elif sub_escolha == 6:
                    segmentos = input("Novos segmentos (separados por vírgula): ").split(", ")
                    aluno.set_segmentos(segmentos)
                elif sub_escolha == 7:
                    turmas = input("Novas turmas (separadas por vírgula): ").split(", ")
                    aluno.set_turmas(turmas)
                elif sub_escolha == 8:
                    username = input("Novo nome de usuário: ")
                    aluno.set_username(username)
                elif sub_escolha == 9:
                    senha = input("Nova senha: ")
                    aluno.set_senha(senha)
                else:
                    print("Opção inválida para edição.")
            
            elif escolha == 2:  # Listar dados
                print("\n--- Dados do Aluno ---")
                print(f"Nome: {aluno.get_nome()} {aluno.get_sobrenome()}")
                print(f"Nome de usuario: {aluno.get_nome_user()}")
                print(f"Endereço: {aluno.get_endereco()}")
                print(f"E-mail: {aluno.get_email()}")
                print(f"E-mail do Responsável: {aluno.get_email_resp()}")
                print(f"Registro Acadêmico: {aluno.get_registro_academ()}")
                print(f"Segmentos: {aluno.get_medio_superior()}")
                print(f"Turma: {aluno.get_turma()}")
                print(f"Ativo: {'Sim' if aluno.get_status() else 'Não'}")
            
            elif escolha == 3:  # Desativar aluno
                aluno.set_status(0)
                print(f"O Aluno:{aluno.get_nome()} {aluno.get_sobrenome()} foi desativado com sucesso.")
            
            elif escolha == 4:  # Reativar aluno
                aluno.set_status(1)
                print(f"O Aluno:{aluno.get_nome()} {aluno.get_sobrenome()} foi reativado com sucesso.")
            
            elif escolha == 5:  # Excluir aluno
                del aluno
                print("Aluno excluído com sucesso. Encerrando menu...")
                break
            
            elif escolha == 6:  # Sair do menu
                print("Saindo...")
                break
            
            else:
                print("Opção inválida, escolha um número entre 1 e 6.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

menu_aluno(aluno1)