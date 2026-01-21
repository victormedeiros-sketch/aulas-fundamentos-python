# Crie uma classe chamada Produto que inclua
# atributos para o nome e a quantidade em
# stock. Utilize a property para aceder a
# quantidade em stock, garantindo que ela nunca
# seja negativa.

# Inclua um métod mostrar_stock
# que exibe uma mensagem indicando quantas
# unidades do produto estão disponíveis.
# Adicione também um métod adicionar_stock que
# permite aumentar a quantidade de stock de um
# produto.


class Produto:
    def __init__(self, nome, stock):
        self.__nome = nome
        if stock >= 0:
            self.__stock = stock
        else:
            self.__stock = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, novo_stock):
        if novo_stock >= 0:
            self.__stock = novo_stock
        else:
            print('Erro. Não é permitido valores negativos')


    def mostrar_stock(self):
        print(f'Produto: {self.__nome} Stock: {self.__stock}')


    def adicionar_stock(self, quantidade):
        if quantidade > 0:
            self.__stock += quantidade
            print(f'{quantidade} unidade(s) adicionada(s) com sucesso')
        else:
            print('A quantidade adicionada deve ser maior que zero.')



produto1 = Produto('Telemovel', 10)

produto1.mostrar_stock()
produto1.adicionar_stock(3)
produto1.mostrar_stock()



