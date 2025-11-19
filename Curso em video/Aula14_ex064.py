#Programa que leia vários números inteiros
#Parar quando for digitado 999
#Quantos numeros foram digitados
#Soma entre eles desconsiderando o 999


numeros = 0
soma_num = 0

num = ''
while num != 999:
    print('Digite um número inteiro de 1 a 998 ou digite 999 para sair do programa')
    num = int(input('---> '))
    numeros += 1
    soma_num += num

print('Concluído!')
print(f'Foram incluídos {numeros - 1} valores')
print(f'A soma dos valores digitados é {soma_num - 999}')