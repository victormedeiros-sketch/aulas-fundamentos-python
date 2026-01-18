# Crie uma classe ContaBancaria com
# atributos privados nib, titular, saldo e
# limite. Adicione métodos getters e
# setters para os atributos.

class Contabancaria:
    def __init__(self, nib, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular


    @property
    def saldo(self):
        return self.__saldo


    @saldo.setter
    def saldo(self, valor):
        self.__saldo += valor


    @property
    def limite(self):
        return self.__limite


minha_conta = Contabancaria('123456789', 'Victor', 1000, 400)
print(f"Titular atual: {minha_conta.titular}")
print(f"Saldo atual: {minha_conta.saldo}")


