from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, endereco: str, email: str, 
                 medio_superior: bool, bacharel_ciencias=False, bacharel_pedago=False, curso="eletro"):
        super().__init__(nome, sobrenome, cpf, endereco, email)
        self.__medio_superior = medio_superior
        if medio_superior:
            self.__curso = curso
        else:
            self.__curso = None 
            self.__bacharel_ciencias = bacharel_ciencias
            self.__bacharel_pedago = bacharel_pedago

    # Getters
    def get_medio_superior(self):
        return self.__medio_superior
     # Retorna None para retornar nada de o aluno é do ensino médio
    def get_curso(self):
        if self.__medio_superior:
            return self.__curso
        return None 

    def get_bacharel_ciencias(self):
        if not self.__medio_superior:
            return self.__bacharel_ciencias
        return None 

    def get_bacharel_pedago(self):
        if not self.__medio_superior:
            return self.__bacharel_pedago
        return None

    # Setters
    def set_medio_superior(self, medio_superior: bool):
        self.__medio_superior = medio_superior
        if medio_superior:
            self.__curso = "mecatrônica"
            self.__bacharel_ciencias = False
            self.__bacharel_pedago = False
        else:
            self.__curso = None
            self.__bacharel_ciencias = False
            self.__bacharel_pedago = False

    def set_curso(self, curso: str):
        if self.__medio_superior:
            if curso in ["mecatrônica", "eletromecânica", "informática"]:
                self.__curso = curso
            else:
                raise ValueError("Curso inválido para o ensino médio.")
        else:
            raise AttributeError("Alunos do ensino superior não possuem 'curso' como no ensino médio.")

    def set_bacharel_ciencias(self, bacharel_ciencias: bool):
        if not self.__medio_superior:
            self.__bacharel_ciencias = bacharel_ciencias
        else:
            raise AttributeError("Alunos do ensino médio não possuem bacharelado em ciências da computação.")

    def set_bacharel_pedago(self, bacharel_pedago: bool):
        if not self.__medio_superior:
            self.__bacharel_pedago = bacharel_pedago
        else:
            raise AttributeError("Alunos do ensino médio não possuem bacharelado em pedagogia.")
