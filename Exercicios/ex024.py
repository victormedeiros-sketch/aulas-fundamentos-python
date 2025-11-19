# Crie um programa que leia um número inteiro introduzido pelo utilizador e que simule um radar de velocidade.
# >80km/h multado
# <=80km/h não multado
# A multa são 100€ + 7€ por cada km/h acima.


print('______RADAR DE VELOCIDADE______')

limite_velocidade = 80
velocidade = int(input('Em que velocidade o veículo passou pelo radar? '))

multa = 100 + 7 * (velocidade - limite_velocidade)

if velocidade > limite_velocidade:
    print('MULTADO')
    print(f'Valor da multa {multa:.2f}')
else:
    print('Não multado! Boa viagem!')





