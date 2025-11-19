print('TABELA DE IDADES')

maior_idade = 0
menor_idade = 0

for c in range(0,7):
    idade = int(input('Digite  sua idade: '))
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'{maior_idade} pessoas são maiores de idade.')
print(f'{menor_idade} pessoas são menores de idade.')