from aluno import Aluno

class Turma:
    def __init__(self, nome: str, 
                 segmento: str, 
                 curso: str, 
                 ano: int, 
                 disciplinas: list,
                 alunos: list,
                 status=1):
        self.__status = status
        self.__nome = nome
        self.__segmento = segmento  # EM ou Superior
        self.__curso = curso
        self.__ano = ano

        if isinstance(disciplinas, list):
            self.__disciplinas = disciplinas
        else:
            self.__disciplinas = [disciplinas]

        if isinstance(alunos, list):
            self.__alunos = alunos
        else:
            self.__alunos = [alunos]

        if self.__segmento == "EM":
            if len(self.__alunos) < 20:
                self.__status = 0
        elif self.__segmento == "Superior":
            if len(self.__alunos) < 5:
                self.__status = 0

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
        total = ""
        for i in self.__disciplinas:
            total += i.get_descricao() + ", "
        return total
    
    def get_alunos(self):
        total = ""
        for i in self.__alunos:
            total += i.get_nome() + ", "
        return total
    
    def get_status(self):
        return self.__status
    
    

    # Setters
    def set_nome(self, novo_nome: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        self.__nome = novo_nome

    def set_segmento(self, novo_segmento: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if novo_segmento in ["EM", "Superior"]:
            self.__segmento = novo_segmento
        else:
            raise ValueError("Segmento inválido. Deve ser 'EM' ou 'Superior'.")

    def set_curso(self, novo_curso: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        self.__curso = novo_curso

    def set_ano(self, novo_ano: int):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(novo_ano, int) and novo_ano > 0:
            self.__ano = novo_ano
        else:
            raise ValueError("O ano deve ser um número inteiro positivo.")

    def set_disciplinas(self, novas_disciplinas: list):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(novas_disciplinas, list):
            self.__disciplinas = novas_disciplinas
        else:
            raise ValueError("As disciplinas devem ser fornecidas como uma lista.")
        
    def set_status(self, status: int):
        if status in [0, 1]:
            self.__status = status
        else:
            raise ValueError("O parâmetro status deve ser 0 ou 1.")
    
    #editar alunos
    def add_alunos(self, novo_aluno: Aluno):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        self.__alunos += novo_aluno
    def remove_aluno(self, remov_aluno: int):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if 0 <= remov_aluno < len(self.__alunos):
            del self.__alunos[remov_aluno]
        else:
            print("Aluno fora da lista")
                
    def validar_turma(self):
        if self.__segmento == "EM":
            if len(self.__alunos) > 20:
                self.__ativo = False
        elif self.__segmento == "Superior":
            if len(self.__alunos) > 5:
                self.__ativo = False

    # def desativar_turma(self):
    #     print("Você deseja desativar a turma?")
    #     escolha=input("Digite 'sim' para confirmar: ")
    #     if escolha == 'sim':
    #         self.__ativo = False
    #     else:
    #         print("Operação cancelada.")