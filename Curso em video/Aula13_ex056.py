# Programa que leia nome idade e sexo de 4 pessoas
# media de idade do grupo
# nome do homem mais velho
# quantas mulheres tem menos de 20 anos

total_idades = 0
idade_homens = 0
homem_mais = ''
mulheres_20 = 0

for c in range(0,4):
    nome = input(f'{c+1}º NOME: ')
    idade = int(input('IDADE: '))
    sexo = input('SEXO(M ou F): ').upper()
    if idade:
        total_idades += idade
    if sexo == 'M' and idade > idade_homens:
        idade_homens = idade
        homem_mais = nome
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1






print(f'A media de idade do grupo é {total_idades / 4} anos')
print(f'{mulheres_20} mulheres tem menos de 20 anos')
print(f'O homem mais velho é {homem_mais} com {idade_homens} anos de idade')