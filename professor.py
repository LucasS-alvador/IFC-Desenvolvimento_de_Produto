from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, formacao, disciplinas:list, segmentos:list, username, senha):
        self.__formacao = formacao
        self.__disciplinas = disciplinas
        self.__segmentos = segmentos
        self.__username = username
        self.__senha = senha