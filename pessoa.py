class Pessoa:
    def __init__(self, nome: str, sobrenome: str, cpf: str, endereco: str, email: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__email = email

    # Getters
    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def get_email(self):
        return self.__email

    # Setters
    def set_nome(self, novo_nome: str):
        self.__nome = novo_nome

    def set_sobrenome(self, novo_sobrenome: str):
        self.__sobrenome = novo_sobrenome

    def set_cpf(self, novo_cpf: str):
        self.__cpf = novo_cpf

    def set_endereco(self, novo_endereco: str):
        self.__endereco = novo_endereco

    def set_email(self, novo_email: str):
        self.__email = novo_email
