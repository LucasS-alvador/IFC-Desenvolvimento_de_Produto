class Turma:
    def __init__(self, nome: str, segmento: str, curso: str, ano: int, disciplinas: list, ativo: bool):
        self.__nome = nome
        self.__segmento = segmento  # EM ou Superior
        self.__curso = curso
        self.__ano = ano
        self.__disciplinas = disciplinas
        self.__ativo = ativo
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
        self.__ativo = ativo



#imprimir, inserir, editar, desativar e excluir uma turma.

def editar_dados(self):
        print("Escolha qual dado deseja editar:")
        print("1 - Nome\n2 - Sobrenome\n3 - CPF\n4 - Endereço\n5 - Email")
        if self.__medio_superior:
            print("6 - Curso")
        else:
            print("6 - Bacharel em Ciências da Computação\n7 - Bacharel em Pedagogia")
        
        escolha = int(input("Digite o número da opção: "))
        if escolha == 1:
            novo_nome = input("Digite o novo nome: ")
            self.set_nome(novo_nome)
        elif escolha == 2:
            novo_segmento = input("Digite o novo segmento: ")
            self.set_segmento(novo_segmento)
        elif escolha == 3:
            novo_curso = input("Digite o novo curso: ")
            self.set_curso(novo_curso)
        elif escolha == 4:
            novo_ano = input("Digite o novo ano: ")
            self.set_ano(novo_ano)
        elif escolha == 5:
            novas_disciplinas = input("Digite a nova disciplina: ")
            self.set_disciplinas(novas_disciplinas)

        else:
            print("Opção inválida.")
            
def excluir_turma(self):
    print("Você deseja excluir a turma?")
    escolha=input("Digite 'sim' para confirmar: ")
    if escolha == 'sim':
        self.__ativo = False
    else:
        print("Operação cancelada.")
