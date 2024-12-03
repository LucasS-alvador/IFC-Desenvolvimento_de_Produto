from pessoa import Pessoa
from turma import Turma

class Professor(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, endereco: str, email: str,
                 formacao: str, disciplinas: list, segmentos: list, username: str, senha: str, turmas: list):
        super().__init__(nome, sobrenome, cpf, endereco, email)
        self.__formacao = formacao
        self.__disciplinas = disciplinas
        self.__segmentos = segmentos
        self.__username = username
        self.__senha = senha
        self.__turmas = turmas
        self.__status = 1
        self.__status = True  # Alterado para booleano

    # Métodos adicionais
    def desativar(self):
        if not self.__status:
            print("O professor já está desativado.")
        else:
            self.__status = False
            print(f"Professor {self.get_nome()} desativado com sucesso.")

    def reativar(self):
        if self.__status:
            print("O professor já está ativo.")
        else:
            self.__status = True
            print(f"Professor {self.get_nome()} reativado com sucesso.")
    # Getters
    def get_formacao(self):
        return self.__formacao

    def get_disciplinas(self):
        return self.__disciplinas

    def get_segmentos(self):
        return self.__segmentos

    def get_username(self):
        return self.__username

    def get_senha(self):
        return self.__senha
    
    def get_turmas(self):
        return self.__turmas
    
    def get_status(self):
        return self.__status

    # Setters
    def set_formacao(self, nova_formacao: str):
        if isinstance(nova_formacao, str) and nova_formacao.strip():
            self.__formacao = nova_formacao
        else:
            raise ValueError("A formação deve ser uma string não vazia.")

    def set_disciplinas(self, novas_disciplinas: list):
        if isinstance(novas_disciplinas, list):
            self.__disciplinas = novas_disciplinas
        else:
            raise ValueError("As disciplinas devem ser fornecidas como uma lista.")

    def set_segmentos(self, novos_segmentos: list):
        if isinstance(novos_segmentos, list):
            self.__segmentos = novos_segmentos
        else:
            raise ValueError("Os segmentos devem ser fornecidos como uma lista.")

    def set_username(self, novo_username: str):
        if isinstance(novo_username, str) and novo_username.strip():
            self.__username = novo_username
        else:
            raise ValueError("O nome de usuário deve ser uma string não vazia.")

    def set_senha(self, nova_senha: str):
        if isinstance(nova_senha, str) and len(nova_senha) >= 6:
            self.__senha = nova_senha
        else:
            raise ValueError("A senha deve ser uma string com pelo menos 6 caracteres.")
        
    def set_turmas(self, nova_turmas: str):
        if isinstance(nova_turmas, list) and nova_turmas.strip():
            self.__turmas = nova_turmas
        else:
            raise ValueError("As turmas devem ser fornecidas como uma lista.")

    # Métodos adicionais
    def desativar(self):
        if self.__status == 0:
            print("O professor já está desativado.")
        else:
            self.__status = 0
            print(f"Professor {self.get_nome()} desativado com sucesso.")

    def reativar(self):
        if self.__status == 1:
            print("O professor já está ativo.")
        else:
            self.__status = 1
            print(f"Professor {self.get_nome()} reativado com sucesso.")

    def excluir(self):
        self.__status = 0
        self.__formacao = None
        self.__disciplinas = []
        self.__segmentos = []
        self.__username = None
        self.__senha = None
        self.__turmas = []
        print(f"Professor {self.get_nome()} {self.get_sobrenome()} excluído com sucesso.")
