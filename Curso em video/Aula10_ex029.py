# Ler a velocidade do carro
# se passar de 80km/h ele é multado
# multa de 7€ por km excedido

from time import sleep

print('---------Radar de velocidade---------')
print('Limite ----------------------80k m/h ')
print('Multa por km excedido ------------ 7€')

veloc = float(input('Velocidade captada pelo radar ---> '))
print('Calculando...')
sleep(2)
print('Aguarde...')
sleep(2)
limite_veloc = 80
km_excedido = veloc - limite_veloc

if veloc > 80:
    print('MUTADO!')
    print(f'Você excedeu {km_excedido}km do permitido.')
    print(f'Multa ---> {km_excedido * 7} € ')

else:
    print('Boa viagem!')
