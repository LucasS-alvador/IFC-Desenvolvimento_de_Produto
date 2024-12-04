from aluno import Aluno
from professor import Professor
from turma import Turma
from diciplina import Disciplina

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
    turmas=["201info","202eletro"])

print(professor1.get_formacao())     
print(professor1.get_disciplinas())  
print(professor1.get_segmentos())    
print(professor1.get_username())     

professor1.set_formacao("Doutorado em Matemática")

print(professor1.get_formacao())  

aluno1 = Aluno(
    nome="João", 
    sobrenome="Silva", 
    cpf="123.456.789-00", 
    endereco="Rua A", 
    email="joao@email.com",
    medio_superior=True, 
    curso="mecatrônica")

print(f"Curso atual: {aluno1._Aluno__curso}") 

print(aluno1.set_curso("informática"))

print(aluno1._Aluno__curso)
choose = 0

 while True:
     if choose == 1:
         novo_c = input("Escolha entre(mecatrônica, eletromecânica, informática)\n")
         try:
             aluno1.set_curso(novo_c)
             print(f"Seu curso agora é {aluno1._Aluno__curso}\n")
         except ValueError:
            print("Houve um erro de digitação\n")
     elif choose == 2:
         print(aluno1)
     elif choose == 3:
         aluno1.editar_dados()

     print("1 - Transferir Curso\n2 - Listar Dados\n3 - Editar Dados\n4 - Desativar Aluno\n5 - Reativar Aluno\n")
     choose = int(input("Oque voçê deseja fazer:"))
     if not isinstance(choose, int) or choose < 1 or choose > 5:
         print("Opção inválida, deve ser um número entre 1 e 5, inclusivo")
        choose = 0

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
                    print("Opção inválida para edição.")
            
            elif escolha == 2:  # Listar dados
                print("\n--- Dados do Professor ---")
                print(f"Nome: {professor.get_username()}")
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
                professor.set_status(0)
                print("Professor desativado com sucesso.")
            
            elif escolha == 4:  # Reativar professor
                professor.set_status(1)
                print("Professor reativado com sucesso.")
            
            elif escolha == 5:  # Excluir professor
                del professor
                print("Professor excluído com sucesso. Encerrando menu...")
                break
            
            elif escolha == 6:  # Sair do menu
                print("Saindo...")
                break
            
            else:
                print("Opção inválida, escolha um número entre 1 e 6.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


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
            escolha = int(input("Escolha uma opção: "))
            
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
                sub_escolha = int(input("Escolha uma opção: "))

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
                    print("Opção inválida para edição.")
            
            elif escolha == 2:  # Listar dados
                print("\n--- Dados do Professor ---")
                print(f"Nome: {professor.get_username()}")
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
                professor.set_status(0)
                print("Professor desativado com sucesso.")
            
            elif escolha == 4:  # Reativar professor
                professor.set_status(1)
                print("Professor reativado com sucesso.")
            
            elif escolha == 5:  # Excluir professor
                del professor
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