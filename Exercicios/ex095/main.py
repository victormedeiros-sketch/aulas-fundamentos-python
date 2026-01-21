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


    def get_nib(self):
        return self.__nib

    def set_nib(self, novo_nib):
        self.__nib = novo_nib


    def get_titular(self):
        return self.__titular

    def set_titular(self, novo_titular):
        self.__titular = novo_titular


    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo = valor


    def get_limite(self):
        return self.__limite

    def set_limite(self, novo_limite):
        self.__limite = novo_limite




minha_conta = Contabancaria('123456789', 'Victor', 1000, 400)


print(f"Titular atual: {minha_conta.get_titular()}")
print(f"Saldo atual: {minha_conta.get_saldo()}")
print(f"Limite: {minha_conta.get_limite()}")


minha_conta.set_titular("Victor Silva")
minha_conta.set_saldo(1500)


print(f"Titular atualizado: {minha_conta.get_titular()}")
print(f"Novo saldo: {minha_conta.get_saldo()}")


