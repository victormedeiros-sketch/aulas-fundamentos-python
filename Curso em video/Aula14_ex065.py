#Ler varios números inteiros introduzidos pelo utilizador
#No final mostrar media entre os numeros
#Qual foi o menor e maior
#O priograma deve perguntar se quer continuar


soma = 0
qtd = 0
resp = 'sim'
media = 0
maior = 0
menor = 0

while resp in 'sim':
    numero = int(input('Digite um número de 1 a 100: '))
    soma += numero
    qtd += 1
    if qtd == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resp = input('Deseja continuar? [sim/nao]').lower().strip()
    media = soma / qtd

print(f'A media dos numeros inseridos foi {media}')
print(f'O menor número foi {menor}')
print(f'O maior número foi {maior}')