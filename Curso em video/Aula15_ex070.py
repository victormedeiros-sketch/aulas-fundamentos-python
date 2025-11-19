# Programa que leia o nome e o preço de vários produtos
# Perguntar sempre se quer continuar
# No final mostre o total gasto na compra
# Quantos produtos custam mais de 1000
# Qual o nome do produto mais barato

total = 0
mais_mil = 0
contador = 0
mais_barato = 0
nome_mb = ''

while True:
    produto = input('Nomo do produto: ')
    preco = float(input('Preço(€): '))
    contador += 1
    total += preco

    if preco > 1000:
        mais_mil = preco

    if contador == 1:
        mais_barato = preco
        nome_mb = produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome_mb = produto


    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('FIM DO PROGRAMA')
print(f'O total da compra foi {total:.2f}')
print(f'{mais_mil} produtos custam mais de mil euros.')
print(f'O produto mais barato foi o {nome_mb} que custa {mais_barato}€')
