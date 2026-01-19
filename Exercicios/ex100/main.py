# Desenvolva uma classe Temperatura que
# armazene a temperatura em graus Celsius como
# um atributo privado. Implemente um getter e
# um setter usando property para permitir que a
# temperatura seja ajustada e lida em Celsius,
# e adicione métodos para converter a
# temperatura para Fahrenheit e Kelvin.

class Temperatura:
    def __init__(self, celcius):
        self.__celcius = celcius


    @property
    def celcius(self):
        return self.__celcius

    @celcius.setter
    def celcius(self, valor):
        self.__celcius = valor


    def mostrar(self):
        print(f'Temperatura: {self.__celcius}ºC')

    def alterar(self, novo_valor):
        self.__celcius = novo_valor
        print(f'Temperatura alterada para {self.__celcius}ºC')

    def converter_kelvin(self):
        return self.__celcius + 273.15


    def converter_farenheit(self):
        return (self.__celcius * 9/5) + 32



temp = Temperatura(25)
temp.mostrar()
temp.alterar(20)
print(f'{temp.converter_kelvin()}ºK')
print(f'{temp.converter_farenheit()}ºF')
