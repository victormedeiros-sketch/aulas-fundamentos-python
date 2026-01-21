# Crie uma classe chamada “Círculo” que
# possua um atributo privado para
# armazenar o raio e métodos getters e
# setters para definir o raio, calcular a
# área e o perímetro do círculo.



import math

class Circulo:
    def __init__(self, raio):
        self.__raio = raio


    def get_raio(self):
        return self.__raio


    def set_raio(self, novo_raio):
        if novo_raio > 0:
            self.__raio = novo_raio
        else:
            print("Erro: O raio deve ser positivo!")

    def calcular_area(self):
        return math.pi * (self.__raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.__raio



meu_circulo = Circulo(5)


print(f"Raio inicial: {meu_circulo.get_raio()}")
print(f"Área: {meu_circulo.calcular_area():.2f}")
print(f"Perímetro: {meu_circulo.calcular_perimetro():.2f}")

print("-" * 20)


meu_circulo.set_raio(15)
print(f"Novo raio: {meu_circulo.get_raio()}")
print(f"Nova área: {meu_circulo.calcular_area():.2f}")





