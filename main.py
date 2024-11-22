class Pessoa():
    def __init__(self, nome:str, sobrenome:str, cpf, endereco:str, email:str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__email = email

class Aluno(Pessoa):

    def __init__(self, medio_superior:bool, bacharel_ciencias = False, bacharel_pedago = False, curso = "eletro"):
        self.__medio_superior = medio_superior #true se médio, false se superior
        if medio_superior:
            self.__curso = curso
        else:
            self.__bacharel_ciencias = bacharel_ciencias
            self.__bacharel_pedago = bacharel_pedago
        
class Professor(Pessoa):
    def __init__(self, formacao, disciplinas:list, segmentos:list, username, senha):
        self.__formacao = formacao
        self.__disciplinas = disciplinas
        self.__segmentos = segmentos
        self.__username = username
        self.__senha = senha

class Turma():
    def __init__(self, nome, segmento, curso, ano, disciplinas:list):
        self.__nome = nome
        self.__segmentos = segmento
        self.__curso = curso
        self.__ano = ano
        self.__disciplinas = disciplinas

class Disciplina():
    def __init__(self, identificador:int, descricao:str, segmento:str, professor:list):
        self.__identificador = identificador
        self.__descricao = descricao
        self.__segmento = segmento
        self.__professor = professor
