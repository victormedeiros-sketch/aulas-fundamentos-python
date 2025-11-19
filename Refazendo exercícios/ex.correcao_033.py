# ler 5 números
# mostrar a soma desses números

soma = 0

for c in range(0,5):
    numero = int(input(f'Digite o {c+1}º número: '))
    soma = soma + numero
    #soma += numero
print(f'A soma dos números é {soma}')


