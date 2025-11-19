# Crie um programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias que foi alugado. Apresente o total a pagar
# carro custa 60€/dia e 0.456€/km.

custo_dia = 60
custo_km = 0.456

dias_aluguel = int(input('Por quantos dias você ficou com o carro alugado? '))
quantidade_km = float(input('Quantos quilometros você rodou com o carro? '))

total = dias_aluguel * custo_dia
total2 = quantidade_km * custo_km

total_geral = total + total2

print('O valor a pagar é ',total_geral,'euros')

