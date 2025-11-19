# 10 números
# quantos deles são pares


contagem_pares = 0
for c in range (0,10):
    numero = int(input(f'Digite o {c+1}º número: '))

    if numero % 2 == 0:
        contagem_pares = contagem_pares + 1

print(f'{contagem_pares} são pares.')






