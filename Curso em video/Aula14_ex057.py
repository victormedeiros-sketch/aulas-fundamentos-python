#Programa que leia o sexo de um apessoa
#Aceite apenas M OU F
#CaSO esteja errado peça de novo ate ter um valor correto

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Sexo(M ou F) : ').upper().strip()
    print('Inválido. Digite novamente!')
print('Bem vindo ')
