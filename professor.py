from pessoa import Pessoa

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
        super().__init__(nome, sobrenome, nome_user, endereco, email, senha, status)  # Inicializa os atributos da classe base
        self.__formacao = formacao
        self.__disciplinas = disciplinas
        self.__segmentos = segmentos
        self.__turmas = turmas
        self.__cpf = cpf

    # Getters
    def get_formacao(self):
        return self.__formacao

    def get_disciplinas(self):
        return self.__disciplinas

    def get_segmentos(self):
        return self.__segmentos
    
    def get_turmas(self):
        return self.__turmas
    
    def get_cpf(self):
        return self.__cpf

    # Setters
    def set_formacao(self, nova_formacao: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(nova_formacao, str) and nova_formacao.strip():
            self.__formacao = nova_formacao
        else:
            raise ValueError("A formação deve ser uma string não vazia.")

    def set_disciplinas(self, novas_disciplinas: list):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(novas_disciplinas, list):
            self.__disciplinas = novas_disciplinas
        else:
            raise ValueError("As disciplinas devem ser fornecidas como uma lista.")

    def set_segmentos(self, novos_segmentos: list):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(novos_segmentos, list):
            self.__segmentos = novos_segmentos
        else:
            raise ValueError("Os segmentos devem ser fornecidos como uma lista.")

    # def set_username(self, novo_username: str):
    #     if isinstance(novo_username, str) and novo_username.strip():
    #         self.__username = novo_username
    #     else:
    #         raise ValueError("O nome de usuário deve ser uma string não vazia.")

    # def set_senha(self, nova_senha: str):
    #     if isinstance(nova_senha, str) and len(nova_senha) >= 6:
    #         self.__senha = nova_senha
    #     else:
    #         raise ValueError("A senha deve ser uma string com pelo menos 6 caracteres.")
        
    def set_turmas(self, nova_turmas: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if isinstance(nova_turmas, list) and nova_turmas.strip():
            self.__turmas = nova_turmas
        else:
            raise ValueError("As turmas devem ser fornecidas como uma lista.")
        
    def set_cpf(self, novo_cpf: str):
        if not self.__status:
            raise Exception("Entidade desativada, valores não podem ser modificados")
        if self.__status:
            self.__cpf = novo_cpf
        else:
            raise Exception("Entidade desativada, valores não podem ser modificados") 
        
    # def set_status(self, novo_status: int):
    #     if novo_status in [0, 1]:
    #         self.__status = novo_status
    #     else:
    #         raise ValueError("O status deve ser 0 ou 1")