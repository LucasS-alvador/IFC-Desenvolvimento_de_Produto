from aluno import Aluno
from professor import Professor
from turma import Turma
from diciplina import Disciplina
from cor import cor
import os

professor1 = Professor(
    nome="Carlos",
    sobrenome="Silva",
    cpf="123.456.789-09",
    endereco="Rua ABC, 123",
    email="carlos@email.com",
    formacao="Mestrado em Matemática",
    disciplinas=["Matemática", "Estatística"],
    segmentos=["EM", "Superior"],
    nome_user="carlos.silva",
    senha="senha123",
    turmas=["201info","302meca"])

professor2 = Professor(
    nome="João",
    sobrenome="Pereira",
    cpf="987.654.321-01",
    endereco="Rua DEF, 456",
    email="joao@email.com",
    formacao="Doutorado em Física",
    disciplinas=["Física", "Química"],
    segmentos=["EM"],
    nome_user="joao.pereira",
    senha="senha456",
    turmas=["301info","302meca"])

aluno1 = Aluno(
    nome="João", 
    sobrenome="Silva", 
    nome_user= "joao123",
    endereco="Rua A", 
    email="joao@email.com",
    senha="1234567890",
    medio_superior=True, 
    status= 1,
    email_resp="paidojoao@gmail.com",
    registro_academ="Joao4321",
    turma="201-MECA",
    bacharel_ciencias=False,
    bacharel_pedago=False,
    curso="mecatrônica")

aluno2 = Aluno(
    nome="Ronaldo",
    sobrenome="Monteiro",
    nome_user= "ronaldomonteiro",
    endereco="Rua B",
    email="ronaldo@email.com",
    senha="1234567890",
    medio_superior=False,
    status= 1,
    email_resp="ronaldomonteiro.mae@gmail.com",
    registro_academ="Ronaldo123",
    turma="202-MECA",
    bacharel_ciencias=True,
    bacharel_pedago=False,
    curso="mecatrônica")

disciplina1 = Disciplina(
    identificador="019273908217301",
    descricao="Matemática",
    segmento="EM",
    professor="Carlos")

disciplina2 = Disciplina(
    identificador="019273908217302",
    descricao="Química",
    segmento="EM",
    professor="João")

turma1 = Turma(
    nome = "MECA 201",
    segmento = "EM",
    ano = 2077,
    curso = "Mecatrônica",
    disciplinas = [disciplina1, disciplina2],
    alunos = [aluno1, aluno2])

professores = [professor1, professor2]
alunos = [aluno1, aluno2]
disciplinas = [disciplina1, disciplina2]
turmas = [turma1]

choose = 0

def menu_aluno(aluno):
    while True:
        print(f"--- {cor['verde']}Menu do Aluno{cor['final']} ---\n")
        print(f"Agora editando: {aluno.get_nome()} {aluno.get_sobrenome()}")
        print("0 - Sair")
        print("1 - Editar Dados")
        print("2 - Listar Dados")
        print("3 - Desativar Aluno")
        print("4 - Reativar Aluno")
        print("5 - Excluir Aluno")
        
        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")

        if escolha == 0:  # Sair do menu
            os.system('cls')
            print(f"{cor['vermelho']}Saindo...{cor['final']}")
            break
    
        elif escolha == 1:  # Editar dados
            print("\n--- Editar Dados ---")
            print("0 - Sair")
            print("1 - Nome e Sobrenome")
            print("2 - Endereço")
            print("3 - E-mail")
            print("4 - E-mail do Responsável")
            print("5 - Registro Acadêmico")
            print("6 - Segmento")
            print("7 - Turma")
            print("8 - Nome de Usuário")
            print("9 - Senha")

            try:
                sub_escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")
            
            if sub_escolha == 0:
                os.system('cls')
                print(f"{cor['vermelho']}Saindo...{cor['final']}")
            elif sub_escolha == 1:
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
                segmento = input("Novo segmento: ")
                aluno.set_medio_superior(segmento)
            elif sub_escolha == 7:
                turma = input("Nova turma: ")
                aluno.set_turma(turma)
            elif sub_escolha == 8:
                username = input("Novo nome de usuário: ")
                aluno.set_nome_user(username)
            elif sub_escolha == 9:
                senha = input("Nova senha: ")
                aluno.set_senha(senha)
            else:
                print(f"Opção inválida para edição.")
        
        elif escolha == 2:  # Listar dados
            print(f"\n--- {cor['verde']}Dados do Aluno{cor['final']} ---\n")
            print(f"Nome: {aluno.get_nome()} {aluno.get_sobrenome()}")
            print(f"Nome de usuario: {aluno.get_nome_user()}")
            print(f"Endereço: {aluno.get_endereco()}")
            print(f"E-mail: {aluno.get_email()}")
            print(f"E-mail do Responsável: {aluno.get_email_resp()}")
            print(f"Registro Acadêmico: {aluno.get_registro_academ()}")
            print(f"Segmentos: {'EM' if aluno.get_medio_superior() else 'Superior'}")
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
        
        
        
        else:
            print(f"{cor['vermelho']}Opção inválida,{cor['final']} escolha um número entre 1 e 6.")

def menu_professor(professor):
    while True:
        print(f"--- {cor['verde']}Menu do Professor{cor['final']} ---\n")
        print(f"Agora editando: {professor.get_nome()} {professor.get_sobrenome()}")
        print("0 - Sair")
        print("1 - Editar Dados")
        print("2 - Listar Dados")
        print("3 - Desativar Professor")
        print("4 - Reativar Professor")
        print("5 - Excluir Professor")

        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")

        if escolha == 0:  # Sair do menu
            os.system('cls')
            print(f"{cor['vermelho']}Saindo...{cor['final']}")
            break 

        elif escolha == 1:  # Editar dados
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

            try:
                sub_escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")            

            if sub_escolha == 0:
                os.system('cls')
                print(f"{cor['vermelho']}Saindo...{cor['final']}")
            elif sub_escolha == 1:
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
            elif sub_escolha ==  5:
                disciplinas = input("Novas disciplinas: ").split(", ")
                professor.set_disciplinas(disciplinas)
            elif sub_escolha ==  6:
                segmentos = input("Novos segmentos spearados por vírgula: ").split(", ")
                professor.set_segmentos(segmentos)
            elif sub_escolha ==  7:
                turmas = input("Novas turmas separadas por vírgula: ").split(", ")
                professor.set_turmas(turmas)
            elif sub_escolha ==  8:
                nome_user = input("Novo nome de usuário: ")
                professor.set_nome_user(nome_user)
            elif sub_escolha ==  9:
                senha = input("Nova senha: ")
                professor.set_senha(senha)
            else:
                print(f"Opção inválida para edição.")
        
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
            print(f"CPF: {professor.get_cpf()}")
            print(f"Nome de Usuário: {professor.get_nome_user()}")
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
        
        else:
            print(f"{cor['vermelho']}Opção inválida,{cor['final']} escolha um número entre 1 e 6.")

def menu_disciplina(disciplina):

    while True:
        print(f"--- {cor['verde']}Menu da Disciplina{cor['final']} ---\n")
        print(f"Agora editando: {disciplina.get_descricao()}")
        print("0 - Sair")
        print("1 - Editar Dados")
        print("2 - Listar Dados")
        print("3 - Desativar Disciplina")
        print("4 - Reativar Disciplina")
        print("5 - Excluir Disciplina")

        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")
        
        if escolha == 1:  # Editar dados
            print("\n--- Editar Dados ---")
            print("0 - Sair")
            print("1 - Identificador")
            print("2 - Descricao")
            print("3 - segmento")
            print("4 - Professor")
            print("5 - Status")

            try:
                sub_escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")
            
            if sub_escolha == 0:
                os.system('cls')
                print(f"{cor['vermelho']}Saindo...{cor['final']}")

            elif sub_escolha == 1:
                identificador = int(input("Novo Identificador: "))
                disciplina.set_identificador(identificador)
            elif sub_escolha == 2:
                descricao = input("Nova Descricao: ")
                disciplina.set_descricao(descricao)
            elif sub_escolha == 3:
                segmentos = input("Novo Segmento: ")
                disciplina.set_segmento(segmentos)
            elif sub_escolha == 4:
                professor = input("Nova formação: ")
                disciplina.set_professor(professor)
            elif sub_escolha == 5:
                status = input("Novo Status:  ")
                disciplina.set_status(status)
            else:
                print("Opção inválida para edição.")
        
        elif escolha == 2:  # Listar dados
            print("\n--- Dados do Disciplina ---")
            print(f"Identificador: {disciplina.get_identificador()}")
            print(f"Descricao: {disciplina.get_descricao()}")
            print(f"Segmento: {disciplina.get_segmento()}")
            print(f"Professor: {disciplina.get_professor()}")
            print(f"Status: {disciplina.get_status()}")
        
        elif escolha == 3:  # Desativar Disciplina
            disciplina.set_status(0)
            print("Disciplina desativada com sucesso.")
        
        elif escolha == 4:  # Reativar Disciplina
            disciplina.set_status(1)
            print("Disciplina reativada com sucesso.")
        
        elif escolha == 5:  # Excluir Disciplina
            del disciplina
            print("Disciplina excluída com sucesso. Encerrando menu...")
            break
        
        elif escolha == 6:  # Sair do menu
            print(f"{cor['vermelho']}Saindo...{cor['final']}")
            break
        
        else:
            print(f"{cor['vermelho']}Opção inválida,{cor['final']} escolha um número entre 1 e 6.")

def menu_turma(turma):
    while True:
        print(f"--- {cor['verde']}Menu da Turma{cor['final']} ---\n")
        print(f"Agora editando: {turma.get_nome()}")
        print("0 - Sair")
        print("1 - Editar Dados")
        print("2 - Listar Dados")
        print("3 - Desativar Turma")
        print("4 - Reativar Turma")
        print("5 - Excluir Turma")

        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")

        if escolha == 0:  # Sair do menu
            os.system('cls')
            print(f"{cor['vermelho']}Saindo...{cor['final']}")
            break
            
        if escolha == 1:  # Editar dados (em casa?) da turma
            print("\n--- Editar Dados ---")
            print("1 - Nome")
            print("2 - Disciplinas")
            print("3 - Segmento")
            print("4 - Curso")
            print("5 - Ano")
            print("6 - Alunos")

            try:
                sub_escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")
            
            if sub_escolha == 0:
                os.system('cls')
                print(f"{cor['vermelho']}Saindo...{cor['final']}")
            elif sub_escolha == 1:
                nome = input("Novo nome: ")
                turma.set_nome(nome)
            elif sub_escolha == 2:
                disciplinas = input("Novas disciplinas (separadas por vírgula): ").split(", ")
                turma.set_disciplinas(disciplinas)
            elif sub_escolha == 3:
                segmento = input("Novo segmento: ")
                turma.set_segmento(segmento)
            elif sub_escolha == 4:
                curso  = input("Novo Curso: ")
                turma.set_curso(curso)
            elif sub_escolha == 5:
                ano = input("Novo ano")
                turma.set_ano(ano)
            elif sub_escolha == 6:
                alunos = input("Novas disciplinas (separadas por vírgula): ").split(", ")
                turma.set_alunos(alunos)
                
            else:
                print("Opção inválida para edição.")
                
        elif escolha == 2: #mostrar dados (em casa?) da turma
            print("\n--- Dados da Turma ---")
            print(f"Nome: {turma.get_nome()}")
            print(f"Curso: {turma.get_curso()}")
            print(f"Segmento: {turma.get_segmento()}")
            print(f"Disciplinas: {turma.get_disciplinas()}")
            print(f"Ano: {turma.get_ano()}")
            print(f"Alunos: {turma.get_alunos()}")
            print(f"Ativa: {'Sim' if turma.get_status() else 'Não'}")
        
        elif escolha == 3:  # Desativar turma
            turma.set_status(0)
            print("Turma desativada com sucesso.")
        
        elif escolha == 4:  # Reativar turma
            turma.set_status(1)
            print("Turma reativada com sucesso.")
        
        elif escolha == 5:  # Excluir turma
            del turma
            print("Turma excluída com sucesso. Encerrando menu...")
        
        else:
            print(f"{cor['vermelho']}Opção inválida,{cor['final']} escolha um número entre 1 e 6.")
    
    #except ValueError:
    #    print(f"{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")

while True:
    escolha = ""
    index = ""

    print(f"--- {cor['verde']}Menu Principal{cor['final']} ---\n")
    print("0 - Sair")
    print("1 - Menu Aluno")
    print("2 - Menu Professor")
    print("3 - Menu Disciplina")
    print("4 - Menu Turma")
    

    try:
        escolha = int(input("\nEscolha uma opção: "))
    except ValueError:
        print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")
    
    os.system('cls')

    # menu aluno
    if escolha == 1:
        print("Escolha qual aluno você deseja acessar:")
        print("0 - Sair")

        for i in range(len(alunos)):
            print(f"{i+1} - {alunos[i].get_nome()}")

        try:
            index = int(input("\nInsira a escolha: "))
        except ValueError:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")

        if index == 0:
            os.system('cls')
            print(f"Saindo do {cor['verde']}menu aluno...{cor['final']}")

        elif index > 0 and index <= len(alunos):
            os.system('cls')
            menu_aluno(alunos[index-1])
        else:
            print(f"\n{cor['vermelho']}Aluno inválido!{cor['final']}")

    # menu professor
    elif escolha == 2:
        print("Escolha qual professor você deseja acessar:")
        print("0 - Sair")

        for i in range(len(professores)):
            print(f"{i+1} - {professores[i].get_nome()}")

        try:
            index = int(input("\nInsira a escolha: ")) 
        except ValueError:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")

        if index == 0:
            os.system('cls')
            print(f"Saindo do {cor['verde']}menu professor...{cor['final']}")

        elif index > 0 and index <= len(professores):
            os.system('cls')
            menu_professor(professores[index-1])
        else:
            print(f"\n{cor['vermelho']}Professor inválido!{cor['final']}")

    # menu disciplina
    elif escolha == 3:
        print("Escolha qual disciplina você deseja acessar:")
        print("0 - Sair")

        for i in range(len(disciplinas)):
            print(f"{i+1} - {disciplinas[i].get_descricao()}")

        try:
            index = int(input("\nInsira a escolha: "))
        except:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")

        if index == 0:
            os.system('cls')
            print(f"Saindo do {cor['verde']}menu disciplina...{cor['final']}")

        elif index > 0 and index <= len(disciplinas):
            os.system('cls')
            menu_disciplina(disciplinas[index-1])
        else:
            print(f"\n{cor['vermelho']}Disciplina inválida!{cor['final']}")
        
    
    # menu turma
    elif escolha == 4:
        print("Escolha qual turma você deseja acessar:")
        print("0 - Sair")
        for i in range(len(turmas)):
            print(f"{i+1} - {turmas[i].get_nome()}")
        
        try:
            index = int(input("\nInsira a escolha: "))
        except:
            print(f"\n{cor['vermelho']}Entrada inválida.{cor['final']} Por favor, digite um número.")
        
        if index == 0:
            os.system('cls')
            print(f"Saindo do {cor['verde']}menu turma...{cor['final']}")

        elif index > 0 and index <= len(turmas):
            os.system('cls')
            menu_turma(turmas[index-1])
        else:
            print(f"\n{cor['vermelho']}Turma inválida!{cor['final']}")
    # sair
    elif escolha == 0:
        print(f"{cor['vermelho']}Saindo...{cor['final']}")
        break

    else:
        print(f"{cor['vermelho']}Opção inválida!{cor['final']}")