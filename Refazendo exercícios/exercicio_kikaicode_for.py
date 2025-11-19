# contagem de 1 a 50
# soma dos pares

numeros_pares = 0

for c in range(0,5):
    print(c+1)
    if c % 2 == 0:
        numeros_pares += c

print(f'A soma dos números pares é {numeros_pares}')

