class Disciplina():
    def __init__(self, identificador:int, descricao:str, segmento:str, professor:list):
        self.__identificador = identificador
        self.__descricao = descricao
        self.__segmento = segmento
        self.__professor = professor