#programa que leia varias notas
#mostre quantas notas inseriu
#mostre a media das notas
#qual a maior nota?
#qual a menor nota

contagem = soma = maior = menor = 0


while True:
    nota = float(input(f'Digite a {contagem+1}ª nota [0 para parar]): '))

    if nota == 0:
        break

    if contagem == 0:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota


    contagem += 1
    soma += nota

media = soma / contagem

print(f'Inseriu {contagem} notas.')
print(f'A maior nota inserida é {maior}')
print(f'A menor nota inserida é {menor}')
print(f'A media das notas é {media}')
