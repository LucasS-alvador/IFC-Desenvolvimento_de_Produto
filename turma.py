class Turma:
    def __init__(self, nome: str, segmento: str, curso: str, ano: int, disciplinas: list):
        self.__nome = nome
        self.__segmento = segmento  # EM ou Superior
        self.__curso = curso
        self.__ano = ano
        self.__disciplinas = disciplinas

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
