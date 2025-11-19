frase = str(input('Digite um frase: ')).strip().upper()
print(f'Quantidade de letras A - {frase.count('A')}')
print(f'Posição em que a letra A aparece pela primeira vez - {frase.find('A')+1}')
print(f'Posição em que a letra A aparece pela ultima vez - {frase.rfind('A')+1}')