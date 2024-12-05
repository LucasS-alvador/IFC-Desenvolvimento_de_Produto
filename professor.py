from pessoa import Pessoa
from cor import cor

class Professor(Pessoa):
    def __init__(self, nome: str, 
                 sobrenome: str, 
                 nome_user: str, 
                 endereco: str, 
                 email: str, 
                 senha:str,
                 #herança de classe pessoa
                 formacao: str, 
                 disciplinas: list, 
                 segmentos: list, 
                 turmas: list, 
                 cpf: str, 
                 status=1):
        
        super().__init__(nome, 
        sobrenome, 
        nome_user, 
        endereco, 
        email, 
        senha, 
        status)  # Inicializa os atributos da classe base
        
        self.__formacao = formacao
        
        if isinstance(disciplinas, list):
            self.__disciplinas = disciplinas
        else:
            self.__disciplinas = [disciplinas]

        if isinstance(segmentos, list):
            self.__segmentos = segmentos
        else:
            self.__segmentos = [segmentos]

        if isinstance(turmas, list):
            self.__turmas = turmas
        else:
            self.__turmas = [turmas]
        self.__cpf = cpf

    # Getters
    def get_formacao(self):
        return self.__formacao

    def get_disciplinas(self):
        total = ""
        for i in self.__disciplinas:
            total += i + ", "
        return total

    def get_segmentos(self):
        total = ""
        for i in self.__segmentos:
            total += i + ", "
        return total
    
    def get_turmas(self):
        total = ""
        for i in self.__turmas:
            total += i + ", "
        return total
    
    def get_cpf(self):
        return self.__cpf

    # Setters
    def set_formacao(self, nova_formacao: str):
        if not self.__status:
            print("Entidade desativada, valores não podem ser modificados")
            return
        if isinstance(nova_formacao, str) and nova_formacao.strip():
            self.__formacao = nova_formacao
        else:
            raise ValueError("A formação deve ser uma string não vazia.")

    def set_disciplinas(self, novas_disciplinas: list):
        if not self.__status:
            print("Entidade desativada, valores não podem ser modificados")
            return
        if isinstance(novas_disciplinas, list):
            self.__disciplinas = novas_disciplinas
        else:
            raise ValueError("As disciplinas devem ser fornecidas como uma lista.")

    def set_segmentos(self, novos_segmentos: list):
        if not self.__status:
            print("Entidade desativada, valores não podem ser modificados")
            return
        if isinstance(novos_segmentos, list):
            self.__segmentos = novos_segmentos
        else:
            raise ValueError("Os segmentos devem ser fornecidos como uma lista.")
        
    def set_turmas(self, nova_turmas: str):
        if not self.__status:
            print("Entidade desativada, valores não podem ser modificados")
            return
        if isinstance(nova_turmas, list) and nova_turmas.strip():
            self.__turmas = nova_turmas
        else:
            raise ValueError("As turmas devem ser fornecidas como uma lista.")
        
    def set_cpf(self, novo_cpf: str):
        if not self.__status:
            print("Entidade desativada, valores não podem ser modificados")
            return
        if self.__status:
            self.__cpf = novo_cpf
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados")