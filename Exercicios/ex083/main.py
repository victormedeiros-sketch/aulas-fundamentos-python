# Escreva um programa que peça ao
# utilizador para inserir dois números e
# divida o primeiro pelo segundo. Utilize
# o tratamento de exceções para lidar com
# casos em que o segundo número é zero e
# quando a entrada não é um número válido.

from uteis import funcoes

funcoes.titulo('SISTEMA DE DIVISÃO')
n1 = funcoes.obter_numero("Digite o primeiro número: ")
n2 = funcoes.obter_numero("Digite o segundo número: ")

funcoes.dividir(n1, n2)


