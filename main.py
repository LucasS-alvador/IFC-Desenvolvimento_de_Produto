class Aluno():
    def __init__(self, nome:str, medio_superior:bool, bacharel_ciencias = False, bacharel_pedago = False, curso = "eletro"):
        self.__nome = nome
        self.__medio_superior = medio_superior #true se médio, false se superior
        if medio_superior:
            self.__curso = curso
        else:
            self.__bacharel_ciencias = bacharel_ciencias
            self.__bacharel_pedago = bacharel_pedago
        
class Profesor():
    def __init__(self, nome, sobrenome, cpf, endereco, formacao, disciplinas:list, segmentos:list, username, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__formacao = formacao
        self.__disciplinas = disciplinas
        self.__segmentos = segmentos
        self.__username = username
        self.__email = email
        self.__senha = senha

class Turma():
    def __init__(self, nome, segmento, curso, ano, disciplinas:list):
        self.__nome = nome
        self.__segmentos = segmento
        self.__curso = curso
        self.__ano = ano
        self.__disciplinas = disciplinas

class Disciplina():
    def __init__(self, id, descricao, segmento, professor):
        pass