#Programa que leia vários números introduzidos pelo utilizador
#O programa só vai parar quando digita 999
#Mostrar quantos foram digitados
#A soma deles descosiderando o flag(último número)

soma = 0
qtd = 0

while True:
    num = int(input('Digite um número de 1 a 100 (ou 999 para parar): '))
    if num == 999:
        break
    soma += num
    qtd += 1

print(f'Foram inseridos {qtd} números e a soma entre eles é {soma}')