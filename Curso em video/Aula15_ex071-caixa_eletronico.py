#Simule um caixa eletronico
#Perguntar qual o valor a ser sacado
#O programa vai informar quantas cedulas de cadavalor serao entregues
#Considere 50,20,10 e 1



saque = int(input('Valor do saque (€): '))
total = saque
cedula = 50
cont_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        cont_cedula += 1

    else:
        if cont_cedula > 0:
            print(f'{cont_cedula} cedulas de {cedula}€')

        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

        cont_cedula = 0
        if total == 0:
            break

print('Volte Sempre! ')



