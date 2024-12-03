from aluno import Aluno
from professor import Professor
from turma import Turma
from diciplina import Disciplina

# Definindo o professor
professor1 = Professor(
    nome="Carlos",
    sobrenome="Silva",
    cpf="123.456.789-09",
    endereco="Rua ABC, 123",
    email="carlos@email.com",
    formacao="Mestrado em Matemática",
    disciplinas=["Matemática", "Estatística"],
    segmentos=["EM", "Superior"],
    username="carlos.silva",
    senha="senha123",
    turmas=["201info", "202eletro"]
)

def menu_professor(professor):
    while True:
        print("\n--- Menu de Opções ---")
        print("1 - Editar Dados")
        print("2 - Listar Dados")   
        print("3 - Desativar Professor")
        print("4 - Reativar Professor")
        print("5 - Excluir Professor")
        print("6 - Sair")

        try:
            escolha = int(input("\nEscolha uma opção: "))
            
            if escolha == 1:  # Editar dados
                print("\n--- Editar Dados ---")
                print("1 - Nome e Sobrenome")
                print("2 - Endereço")
                print("3 - E-mail")
                print("4 - Formação")
                print("5 - Disciplinas")
                print("6 - Segmentos")
                print("7 - Turmas")
                print("8 - Nome de Usuário")
                print("9 - Senha")
                sub_escolha = int(input("\n Escolha uma opção: "))

                if sub_escolha == 1:
                    nome = input("Novo nome: ")
                    sobrenome = input("Novo sobrenome: ")
                    professor.set_nome(nome)
                    professor.set_sobrenome(sobrenome)
                elif sub_escolha == 2:
                    endereco = input("Novo endereço: ")
                    professor.set_endereco(endereco)
                elif sub_escolha == 3:
                    email = input("Novo e-mail: ")
                    professor.set_email(email)
                elif sub_escolha == 4:
                    formacao = input("Nova formação: ")
                    professor.set_formacao(formacao)
                elif sub_escolha == 5:
                    disciplinas = input("Novas disciplinas (separadas por vírgula): ").split(", ")
                    professor.set_disciplinas(disciplinas)
                elif sub_escolha == 6:
                    segmentos = input("Novos segmentos (separados por vírgula): ").split(", ")
                    professor.set_segmentos(segmentos)
                elif sub_escolha == 7:
                    turmas = input("Novas turmas (separadas por vírgula): ").split(", ")
                    professor.set_turmas(turmas)
                elif sub_escolha == 8:
                    username = input("Novo nome de usuário: ")
                    professor.set_username(username)
                elif sub_escolha == 9:
                    senha = input("Nova senha: ")
                    professor.set_senha(senha)
                else:
                    print("\n  Opção inválida para edição.")
            
            elif escolha == 2:  # Listar dados
                print("\n--- Dados do Professor ---")
                print(f"Nome: {professor.get_nome()} {professor.get_sobrenome()}")
                print(f"CPF: {professor.get_cpf()}")
                print(f"Endereço: {professor.get_endereco()}")
                print(f"E-mail: {professor.get_email()}")
                print(f"Formação: {professor.get_formacao()}")
                print(f"Disciplinas: {professor.get_disciplinas()}")
                print(f"Segmentos: {professor.get_segmentos()}")
                print(f"Turmas: {professor.get_turmas()}")
                print(f"Nome de Usuário: {professor.get_username()}")
                print(f"Ativo: {'Sim' if professor.get_status() else 'Não'}")
            
            elif escolha == 3:  # Desativar professor
                professor.desativar()
                print("Professor desativado com sucesso.")
            
            elif escolha == 4:  # Reativar professor
                professor.reativar()
                print("Professor reativado com sucesso.")
            
            elif escolha == 5:  # Excluir professor
                professor.excluir()
                print("Professor excluído com sucesso. Encerrando menu...")
                break
            
            elif escolha == 6:  # Sair do menu
                print("Saindo...")
                break
            
            else:
                print("Opção inválida, escolha um número entre 1 e 6.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Chamando o menu para o professor
menu_professor(professor1)
