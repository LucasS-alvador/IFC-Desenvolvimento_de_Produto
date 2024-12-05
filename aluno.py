from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str,
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
                 status=1):
        
        super().__init__(nome, sobrenome, nome_user, endereco, email, senha, status)
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
    def get_status(self):
        return self.__status

    # Setters
    def set_medio_superior(self, novo_medio_superior: bool):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        self.__medio_superior = novo_medio_superior
        if novo_medio_superior:
            self.__curso = "mecatrônica"
            self.__bacharel_ciencias = False
            self.__bacharel_pedago = False
        else:
            self.__curso = None
            self.__bacharel_ciencias = False
            self.__bacharel_pedago = False
        
    def set_email_resp(self, novo_email_resp):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        self.__email_resp = novo_email_resp
    
    def set_registro_academ(self, novo_registro):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        self.__registro_academ = novo_registro
    
    def set_turma(self, nova_turma):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        self.__turma = nova_turma
    
    #def set_curso(self):
    #    if not self.__status:
    #        raise Exception("Entidade desativada, valores não podem ser modificados")
    #    if self.__medio_superior:
    #        return self.__curso
    #    return None 
    
    def set_curso(self, curso: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if self.__medio_superior:
            if curso in ["mecatrônica", "eletromecânica", "informática"]:
                self.__curso = curso
            else:
                raise ValueError("Curso inválido para o ensino médio.")
        else:
            raise AttributeError("Alunos do ensino superior não possuem 'curso' como no ensino médio.")

    def set_bacharel_ciencias(self, bacharel_ciencias: bool):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if not self.__medio_superior:
            self.__bacharel_ciencias = bacharel_ciencias
        else:
            raise AttributeError("Alunos do ensino médio não possuem bacharelado em ciências da computação.")

    def set_bacharel_pedago(self, bacharel_pedago: bool):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if not self.__medio_superior:
            self.__bacharel_pedago = bacharel_pedago
        else:
            raise AttributeError("Alunos do ensino médio não possuem bacharelado em pedagogia.")

    def set_status(self, novo_status):
        if novo_status in [0, 1]:
            self.__status = novo_status
        else:
            print("Status deve ser 0 ou 1")
    # def __str__(self):
    #     return f'''
    #     Nome:{self.get_nome()}
    #     Sobrenome:{self.get_sobrenome()}
    #     Cpf:{self.get_cpf()}
    #     Endereco:{self.get_endereco()}
    #     Email:{self.get_endereco()}
    #     Ensino Médio:{self.__medio_superior}
    #     bacharel_ciencias:{self.get_bacharel_ciencias()}
    #     bacharel_pedago:{self.get_bacharel_pedago()}
    #     curso:{self.__curso}
    #     '''

    # def editar_dados(self):
    #     print("Escolha qual dado deseja editar:")
    #     print("1 - Nome\n2 - Sobrenome\n3 - CPF\n4 - Endereço\n5 - Email")
    #     if self.__medio_superior:
    #         print("6 - Curso")
    #     else:
    #         print("6 - Bacharel em Ciências da Computação\n7 - Bacharel em Pedagogia")
        
    #     escolha = int(input("Digite o número da opção: "))
    #     if escolha == 1:
    #         novo_nome = input("Digite o novo nome: ")
    #         self.set_nome(novo_nome)
    #     elif escolha == 2:
    #         novo_sobrenome = input("Digite o novo sobrenome: ")
    #         self.set_sobrenome(novo_sobrenome)
    #     elif escolha == 3:
    #         novo_cpf = input("Digite o novo CPF: ")
    #         self.set_cpf(novo_cpf)
    #     elif escolha == 4:
    #         novo_endereco = input("Digite o novo endereço: ")
    #         self.set_endereco(novo_endereco)
    #     elif escolha == 5:
    #         novo_email = input("Digite o novo email: ")
    #         self.set_email(novo_email)
    #     elif escolha == 6:
    #         if self.__medio_superior:
    #             novo_curso = input("Digite o novo curso (mecatrônica, eletromecânica, informática): ")
    #             self.set_curso(novo_curso)
    #         else:
    #             novo_ciencia = input("Cursará Bacharel em Ciências da Computação? (sim/não): ").strip().lower() == "sim"
    #             self.set_bacharel_ciencias(novo_ciencia)
    #     elif escolha == 7 and not self.__medio_superior:
    #         novo_pedagogia = input("Cursará Bacharel em Pedagogia? (sim/não): ").strip().lower() == "sim"
    #         self.set_bacharel_pedago(novo_pedagogia)
    #     else:
    #         print("Opção inválida.")
