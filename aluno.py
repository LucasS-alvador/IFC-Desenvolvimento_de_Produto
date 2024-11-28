from pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, medio_superior:bool, bacharel_ciencias = False, bacharel_pedago = False, curso = "eletro"):
        self.__medio_superior = medio_superior #true se médio, false se superior
        if medio_superior:
            self.__curso = curso
        else:
            self.__bacharel_ciencias = bacharel_ciencias
            self.__bacharel_pedago = bacharel_pedago