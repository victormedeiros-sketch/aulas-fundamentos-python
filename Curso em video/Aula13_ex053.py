frase = input('Digite uma frase: ').strip().lower().replace(' ','')
if frase[::-1] == frase:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
