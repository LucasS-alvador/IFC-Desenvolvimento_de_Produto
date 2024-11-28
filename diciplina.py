class Disciplina:
    def __init__(self, identificador: int, descricao: str, segmento: str, professor: list):
        self.__identificador = identificador
        self.__descricao = descricao
        self.__segmento = segmento  # EM ou Superior
        self.__professor = professor

    # Getters
    def get_identificador(self):
        return self.__identificador

    def get_descricao(self):
        return self.__descricao

    def get_segmento(self):
        return self.__segmento

    def get_professor(self):
        return self.__professor

    # Setters
    def set_identificador(self, novo_identificador: int):
        if isinstance(novo_identificador, int) and novo_identificador > 0:
            self.__identificador = novo_identificador
        else:
            raise ValueError("O identificador deve ser um número inteiro positivo.")

    def set_descricao(self, nova_descricao: str):
        if isinstance(nova_descricao, str) and nova_descricao.strip():
            self.__descricao = nova_descricao
        else:
            raise ValueError("A descrição deve ser uma string não vazia.")

    def set_segmento(self, novo_segmento: str):
        if novo_segmento in ["EM", "Superior"]:
            self.__segmento = novo_segmento
        else:
            raise ValueError("Segmento inválido. Deve ser 'EM' ou 'Superior'.")

    def set_professor(self, novo_professor: list):
        if isinstance(novo_professor, list):
            self.__professor = novo_professor
        else:
            raise ValueError("Os professores devem ser fornecidos como uma lista.")
