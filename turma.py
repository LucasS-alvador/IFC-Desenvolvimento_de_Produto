from aluno import Aluno

class Turma:
    def __init__(self, nome: str, 
                 segmento: str, 
                 curso: str, 
                 ano: int, 
                 disciplinas: list,
                 alunos: list,
                 ativo: bool):
        self.__ativo = ativo
        self.__nome = nome
        self.__segmento = segmento  # EM ou Superior
        self.__curso = curso
        self.__ano = ano
        self.__disciplinas = disciplinas
        self.__alunos = alunos

        if self.__segmento == "EM":
            if len(self.__alunos) > 20:
                self.__ativo = False
        elif self.__segmento == "Superior":
            if len(self.__alunos) > 5:
                self.__ativo = False

    # Getters
    def get_nome(self):
        return self.__nome

    def get_segmento(self):
        return self.__segmento

    def get_curso(self):
        return self.__curso

    def get_ano(self):
        return self.__ano

    def get_disciplinas(self):
        return self.__disciplinas
    
    def get_alunos(self):
        return self.__alunos
    
    def get_ativo(self):
        return self.__ativo
    
    

    # Setters
    def set_nome(self, novo_nome: str):
        self.__nome = novo_nome

    def set_segmento(self, novo_segmento: str):
        if novo_segmento in ["EM", "Superior"]:
            self.__segmento = novo_segmento
        else:
            raise ValueError("Segmento inválido. Deve ser 'EM' ou 'Superior'.")

    def set_curso(self, novo_curso: str):
        self.__curso = novo_curso

    def set_ano(self, novo_ano: int):
        if isinstance(novo_ano, int) and novo_ano > 0:
            self.__ano = novo_ano
        else:
            raise ValueError("O ano deve ser um número inteiro positivo.")

    def set_disciplinas(self, novas_disciplinas: list):
        if isinstance(novas_disciplinas, list):
            self.__disciplinas = novas_disciplinas
        else:
            raise ValueError("As disciplinas devem ser fornecidas como uma lista.")
        
    def set_ativo(self, ativo: bool):
        if isinstance(ativo, bool):
            self.__ativo = ativo
        else:
            raise ValueError("O parâmetro ativo deve ser um valor booleano.")
    
    #editar alunos
    def add_alunos(self, novo_aluno: Aluno):
        self.__alunos += novo_aluno
    def remove_aluno(self, remov_aluno: int):
        del self.__alunos[remov_aluno]
                
    def validar_turma(self):
        if self.__segmento == "EM":
            if len(self.__alunos) > 20:
                self.__ativo = False
        elif self.__segmento == "Superior":
            if len(self.__alunos) > 5:
                self.__ativo = False
            
    def desativar_turma(self):
        print("Você deseja desativar a turma?")
        escolha=input("Digite 'sim' para confirmar: ")
        if escolha == 'sim':
            self.__ativo = False
        else:
            print("Operação cancelada.")

    def imprimir_turma(self):
        imp_turma = input("Digite o nome da turma que deseja imprimir: ")
        if imp_turma == self.__nome:
            return(self.__nome, self.__segmento, self.__curso, self.__ano, self.__disciplinas, self.__ativo)


                
