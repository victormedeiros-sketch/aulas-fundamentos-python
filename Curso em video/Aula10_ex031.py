# Ler a distancia de uma viagem percorrida em km
# preço da passagem é 0,50 por km para viagens de até 200km
# preço da passagem é 0,45 por km para viagens mais longas
from time import sleep
print('-----------Calculo de passagem----------')
print('Digite a distancia da sua viagem em km:')
distancia = float(input('(km)--->'))
print('----------------------------------------')
print('Calculando...')
sleep(2)
preco_min = 0.45
preco_max = 0.50
km_min = 200

if distancia <= km_min:
    print(f'Para a distancia de {distancia}km o valor da passagem é {distancia * preco_max}€')

else:
    print(f'Para a distancia de {distancia}km o valor da passagem é {distancia * preco_min}€')

