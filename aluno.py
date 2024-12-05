from pessoa import Pessoa
from cor import cor

class Aluno(Pessoa):
    def __init__(self, 
                 nome: str,
                 sobrenome: str, 
                 nome_user: str, 
                 endereco: str,
                 email: str, 
                 senha:str,
                 #herança de classe pessoa
                 medio_superior: bool, 
                 email_resp: str, 
                 registro_academ: str,
                 turma: str, 
                 bacharel_ciencias=False, 
                 bacharel_pedago=False, 
                 curso="mecatrônica", 
                 status = 1
                 ):
        
        super().__init__(nome, 
        sobrenome, 
        nome_user, 
        endereco, 
        email, 
        senha, 
        status)
        
        self.__medio_superior = medio_superior
        self.__email_resp = email_resp
        self.__registro_academ = registro_academ
        self.__turma = turma
        if medio_superior:
            self.__curso = curso
        else:
            self.__curso = None 
            self.__bacharel_ciencias = bacharel_ciencias
            self.__bacharel_pedago = bacharel_pedago

    # Getters
    def get_medio_superior(self):
        return self.__medio_superior
     # Retorna None para retornar nada se o aluno é do ensino médio

    def get_email_resp(self):
        return self.__email_resp
    
    def get_registro_academ(self):
        return self.__registro_academ
    
    def get_turma(self):
        return self.__turma
    
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
    def set_medio_superior(self, novo_medio_superior: bool):
        if not self.__status:
            print(f"Entidade desativada, valores não podem ser modificados")
            return
        self.__medio_superior = novo_medio_superior
        if novo_medio_superior:
            self.__curso = "mecatrônica"
            self.__bacharel_ciencias = False
            self.__bacharel_pedago = False
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            self.__curso = None
            self.__bacharel_ciencias = False
            self.__bacharel_pedago = False
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        
    def set_email_resp(self, novo_email_resp):
        if not self.__status:
            print(f"Entidade desativada, valores não podem ser modificados")
            return
        self.__email_resp = novo_email_resp
        print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
    
    def set_registro_academ(self, novo_registro):
        if not self.__status:
            print(f"Entidade desativada, valores não podem ser modificados")
            return
        self.__registro_academ = novo_registro
        print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
    
    def set_turma(self, nova_turma):
        if not self.__status:
            print(f"Entidade desativada, valores não podem ser modificados")
            return
        self.__turma = nova_turma
        print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
    
    def set_curso(self, curso: str):
        if not self.__status:
            print(f"Entidade desativada, valores não podem ser modificados")
            return
        if self.__medio_superior:
            if curso in ["mecatrônica", "eletromecânica", "informática"]:
                self.__curso = curso
                print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
            else:
                raise ValueError(f"Curso inválido para o ensino médio.")
        else:
            raise AttributeError(f"Alunos do ensino superior não possuem 'curso' como no ensino médio.")

    def set_bacharel_ciencias(self, bacharel_ciencias: bool):
        if not self.__status:
            print(f"Entidade desativada, valores não podem ser modificados")
            return
        if not self.__medio_superior:
            self.__bacharel_ciencias = bacharel_ciencias
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise AttributeError(f"Alunos do ensino médio não possuem bacharelado em ciências da computação.")

    def set_bacharel_pedago(self, bacharel_pedago: bool):
        if not self.__status:
            print(f"Entidade desativada, valores não podem ser modificados")
            return
        if not self.__medio_superior:
            self.__bacharel_pedago = bacharel_pedago
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise AttributeError(f"Alunos do ensino médio não possuem bacharelado em pedagogia.")

aluno1 = Aluno(
    nome="João", 
    sobrenome="Silva", 
    nome_user= "joao123",
    endereco="Rua A", 
    email="joao@email.com",
    senha="1234567890",
    medio_superior=True, 
    status=1,
    email_resp="paidojoao@gmail.com",
    registro_academ="Joao4321",
    turma="201-MECA",
    bacharel_ciencias=False,
    bacharel_pedago=False,
    curso="mecatrônica"
)
aluno1.get_status()