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
        if not self.get_status():
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if isinstance(nova_formacao, str) and nova_formacao.strip():
            self.__formacao = nova_formacao
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}A formação deve ser uma string não vazia.{cor['final']}")

    def set_disciplinas(self, novas_disciplinas: list):
        if not self.get_status():
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if isinstance(novas_disciplinas, list):
            self.__disciplinas = novas_disciplinas
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}As disciplinas devem ser fornecidas como uma lista.{cor['final']}")

    def set_segmentos(self, novos_segmentos: list):
        if not self.get_status():
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if isinstance(novos_segmentos, list):
            self.__segmentos = novos_segmentos
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}Os segmentos devem ser fornecidos como uma lista.{cor['final']}")

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
        if not self.get_status():
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if isinstance(nova_turmas, list) and nova_turmas.strip():
            self.__turmas = nova_turmas
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}As turmas devem ser fornecidas como uma lista.{cor['fianl']}")
        
    def set_cpf(self, novo_cpf: str):
        if not self.get_status():
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if self.__status:
            self.__cpf = novo_cpf
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}") 
        
    # def set_status(self, novo_status: int):
    #     if novo_status in [0, 1]:
    #         self.__status = novo_status
    #     else:
    #         raise ValueError("O status deve ser 0 ou 1")
