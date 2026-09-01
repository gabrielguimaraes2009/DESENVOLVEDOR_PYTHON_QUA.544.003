from abc import ABC, abstractmethod


class IConta(ABC):

    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def gerar_extrato(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


class Pessoa:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def __str__(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}"


class Conta(IConta):

    def __init__(self, titular, agencia, n_conta, saldo):
        self.__titular = titular
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    def consultar_dados(self):
        print(f"Titular: {self.__titular}")
        print(f"Agência: {self.__agencia}")
        print(f"Número da conta: {self.__n_conta}")
        print(f"Saldo: R$ {self.__saldo:.2f}")

    def gerar_extrato(self):
        print("====== EXTRATO ======")
        print(f"Titular: {self.__titular}")
        print(f"Agência: {self.__agencia}")
        print(f"Número da conta: {self.__n_conta}")
        print(f"Saldo: R$ {self.__saldo:.2f}")
        print("=====================")

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo

    def sacar(self, valor):
        self.__saldo -= valor
        return self.__saldo