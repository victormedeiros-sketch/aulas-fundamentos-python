#programa que mostre a tabuada do numero inserido pelo utilizador
#programa será interrompido quando o numero inserido for negativo ou 0

print('TABUADA:')

while True:
    numero = int(input('Digite um número: '))
    if numero  <= 0:
        break

    for c in range(0,10):
        print(f'{numero} x {c +1} = {numero * (c+1)}')

print('fim')