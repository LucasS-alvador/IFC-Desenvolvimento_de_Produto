class Pessoa:
    def __init__(self, 
                 nome: str, 
                 sobrenome: str, 
                 nome_user: str,
                 endereco: str, 
                 email: str, 
                 senha:str, 
                 status):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nome_user = nome_user
        self.__endereco = endereco
        self.__email = email
        self.__senha = senha
        self.__status = status

    # Getters
    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome
    
    def get_nome_user(self):
        return self.__nome_user

    def get_endereco(self):
        return self.__endereco

    def get_email(self):
        return self.__email
    
    def get_senha(self):
        return self.__senha
    
    def get_status(self):
        return self.__status

    # Setters
    
    def set_nome(self, novo_nome: str):
        if self.__status:
            self.__nome = novo_nome
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados")

    def set_sobrenome(self, novo_sobrenome: str):
        if self.__status:
            self.__sobrenome = novo_sobrenome
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados")        

    def set_nome_user(self, novo_nome_user):
        if self.__status:
            self.__nome_user = novo_nome_user
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados") 

    def set_endereco(self, novo_endereco: str):
        if self.__status:
            self.__endereco = novo_endereco
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados") 

    def set_email(self, novo_email: str):
        if self.__status:
            self.__email = novo_email
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        
    def set_senha(self, nova_senha: str):
        if self.__status:
            self.__senha = nova_senha
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados")
    
    def set_status(self, novo_status):
        if novo_status in [0, 1]:
            self.__status = novo_status
        else:
            print("Status deve ser 0 ou 1")