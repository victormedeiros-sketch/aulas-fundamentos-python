# Mostrar a tabuada de um número introduzido pelo utilizador.

print('---TABUADA---')

num = int(input('Digite um número: '))
for c in range(0,10):
    print(f'{c+1} x {num} = {(c+1) * num}')


