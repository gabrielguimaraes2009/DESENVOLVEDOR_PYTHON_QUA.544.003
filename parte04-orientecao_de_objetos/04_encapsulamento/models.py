class Pessoa:
    def __init__(self, nome, telefone, cpf, email):
        self.__nome = nome 
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone

    # métodos de acesso
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade >= 0:
            self.__idade = nova_idade
        else:
            raise ValueError("Idade deve ser um número inteiro não negativo.")