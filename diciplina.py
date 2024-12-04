class Disciplina:
    def __init__(self, identificador: int, 
                 descricao: str, 
                 segmento: list, 
                 professor: list, 
                 status=1):
        self.__identificador = identificador
        self.__descricao = descricao
        self.__segmento = segmento  # EM ou Superior
        self.__professor = professor
        self.__status = status

    # Getters
    def get_identificador(self):
        return self.__identificador

    def get_descricao(self):
        return self.__descricao

    def get_segmento(self):
        return self.__segmento

    def get_professor(self):
        return self.__professor
    
    def get_status(self):
        return self.__status

    # Setters
    def set_identificador(self, novo_identificador: int):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(novo_identificador, int) and novo_identificador > 0:
            self.__identificador = novo_identificador
        else:
            raise ValueError("O identificador deve ser um número inteiro positivo.")

    def set_descricao(self, nova_descricao: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(nova_descricao, str) and nova_descricao.strip():
            self.__descricao = nova_descricao
        else:
            raise ValueError("A descrição deve ser uma string não vazia.")

    def set_segmento(self, novos_segmentos: list):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if all(i in ["EM", "Superior"] for i in novos_segmentos):
            self.__segmento = novos_segmentos
        else:
            raise ValueError("Segmentos inválidos. Devem ser 'EM' ou 'Superior'.")

    def set_professor(self, novo_professor: list):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(novo_professor, list):
            self.__professor = novo_professor
        else:
            raise ValueError("Os professores devem ser fornecidos como uma lista.")
        
    def set_status(self, novo_status):
        if novo_status in [0,1]:
            self.__status = novo_status
