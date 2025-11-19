#Pedir o peso de 5 pessoas
#Mostrar o maior e menor peso lido

maior_peso = 0
menor_peso = 0

for c in range(0,5):
    peso = float(input(f'Digite o peso da {c+1}ª pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso

    else:
        if peso > maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

print(f'O menor peso é {menor_peso}')
print(f'O maior peso é {maior_peso}')

