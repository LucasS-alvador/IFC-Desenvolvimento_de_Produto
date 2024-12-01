from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, endereco: str, email: str,status:bool, medio_superior: bool, bacharel_ciencias=False, bacharel_pedago=False, curso="eletro"):
        super().__init__(nome, sobrenome, cpf, endereco, email)
        self.__medio_superior = medio_superior
        self.__status = status
        if medio_superior:
            self.__curso = curso
        else:
            self.__curso = None 
            self.__bacharel_ciencias = bacharel_ciencias
            self.__bacharel_pedago = bacharel_pedago

    # Getters
    def get_status(self):
        return self.__status
    
    def get_medio_superior(self):
        return self.__medio_superior
     # Retorna None para retornar nada se o aluno é do ensino médio
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
    def set_status(self,status:bool):
        self.__status = status

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

    def __str__(self):
        if self.__status:
            return f'''
            Nome:{self.get_nome()}
            Sobrenome:{self.get_sobrenome()}
            Cpf:{self.get_cpf()}
            Endereco:{self.get_endereco()}
            Email:{self.get_endereco()}
            Ensino Médio:{self.__medio_superior}
            bacharel_ciencias:{self.get_bacharel_ciencias()}
            bacharel_pedago:{self.get_bacharel_pedago()}
            curso:{self.__curso}
            '''
        return "O aluno atualmente se encontra desativado\n"

    def editar_dados(self):
        if self.__status:
            print("Escolha qual dado deseja editar:")
            print("1 - Nome\n2 - Sobrenome\n3 - CPF\n4 - Endereço\n5 - Email")
            if self.__medio_superior:
                print("6 - Curso")
            else:
                print("6 - Bacharel em Ciências da Computação\n7 - Bacharel em Pedagogia")
        
            escolha = int(input("Digite o número da opção: "))
            if escolha == 1:
                novo_nome = input("Digite o novo nome: ")
                self.set_nome(novo_nome)
            elif escolha == 2:
                novo_sobrenome = input("Digite o novo sobrenome: ")
                self.set_sobrenome(novo_sobrenome)
            elif escolha == 3:
                novo_cpf = input("Digite o novo CPF: ")
                self.set_cpf(novo_cpf)
            elif escolha == 4:
                novo_endereco = input("Digite o novo endereço: ")
                self.set_endereco(novo_endereco)
            elif escolha == 5:
                novo_email = input("Digite o novo email: ")
                self.set_email(novo_email)
            elif escolha == 6:
                if self.__medio_superior:
                   novo_curso = input("Digite o novo curso (mecatrônica, eletromecânica, informática): ")
                   self.set_curso(novo_curso)
                else:
                    novo_ciencia = input("Cursará Bacharel em Ciências da Computação? (sim/não): ").strip().lower() == "sim"
                    self.set_bacharel_ciencias(novo_ciencia)
            elif escolha == 7 and not self.__medio_superior:
                novo_pedagogia = input("Cursará Bacharel em Pedagogia? (sim/não): ").strip().lower() == "sim"
                self.set_bacharel_pedago(novo_pedagogia)
            else:
                print("Opção inválida.")
        else:
            "O aluno atualmente se encontra desativado\n"
