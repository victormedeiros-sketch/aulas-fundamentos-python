# Crie uma classe chamada “Círculo” que
# possua um atributo privado para
# armazenar o raio e métodos getters e
# setters para definir o raio, calcular a
# área e o perímetro do círculo.



class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, novo_raio):
        if novo_raio > 0:
            self.__raio = novo_raio
        else:
            print("O raio deve ser positivo!")

    def calcular_area(self):
        return 3.14 * (self.__raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.__raio



meu_circulo = Circulo(5)
area = meu_circulo.calcular_area()
perimetro = meu_circulo.calcular_perimetro()


print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")


meu_circulo.raio(float(input('Digite o novo raio: ')))
print(f"Nova área: {meu_circulo.calcular_area():.2f}")





