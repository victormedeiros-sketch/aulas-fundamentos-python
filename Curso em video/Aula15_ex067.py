#Programa que leia a tabuada de vários números
#um de cada vez para cada valor
#O programa será interrompido quando o número solicitado for negativo



while True:

    numero = int(input('Digite um úmero para exibir a sua tabuada: '))
    print('_' * 20)
    if numero < 0:
        break
    print('----Tabuada----')
    print('_' * 20)
    for c in range(0, 10):
        print(f'{numero} x {c+1} = {numero * (c+1)}')




print('Programa finalizado.')



