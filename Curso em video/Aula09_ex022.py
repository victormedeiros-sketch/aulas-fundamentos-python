nome = input('Qual o seu nome completo? ').strip()
print('Nome em maiusculo - ',nome.upper())
print('Nome em minusculo - ',nome.lower())

print('Quantidade de letras')
print(len(nome.replace(' ','')))
print('Quantidade de letras do primeiro nome')
espaco = ' '
print(f'O seu primeiro nome tem {nome.find(' ')}')



