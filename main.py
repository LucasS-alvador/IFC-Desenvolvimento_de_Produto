from aluno import Aluno
from professor import Professor
from turma import Turma
from diciplina import Disciplina

# professor1 = Professor(
#     nome="Carlos",
#     sobrenome="Silva",
#     cpf="123.456.789-09",
#     endereco="Rua ABC, 123",
#     email="carlos@email.com",
#     formacao="Mestrado em Matemática",
#     disciplinas=["Matemática", "Estatística"],
#     segmentos=["EM", "Superior"],
#     username="carlos.silva",
#     senha="senha123")

# print(professor1.get_formacao())     
# print(professor1.get_disciplinas())  
# print(professor1.get_segmentos())    
# print(professor1.get_username())     

# professor1.set_formacao("Doutorado em Matemática")

# print(professor1.get_formacao())  

aluno1 = Aluno(nome="João", sobrenome="Silva", cpf="123.456.789-00", endereco="Rua A", email="joao@email.com",medio_superior=True, curso="mecatrônica")

# print(f"Curso atual: {aluno1._Aluno__curso}") 

# print(aluno1.set_curso("informática"))

# print(aluno1._Aluno__curso)
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
