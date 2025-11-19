#   programa que leia varios números inteiros
#   terminar apenas quando o utilizador digitar a opção parar
#   no final mostre quantos números o utilizador inseriu
#   e qual a soma deles

soma = 0
contador = 0

while True:
    numero = int(input('Digite um número ou 0 para parar: '))
    if numero  == 0:
        break

    soma += numero
    contador += 1

print(f'A soma entre os valores é {soma}')
print(f'Foram inseridos {contador} valores')




