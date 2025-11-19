# Crie um programa que tenha uma tuple com nomes de jogos e os seus respectivos preços em sequência.
# No final mostre a listagem de perços organizados como tabela

jogos = 'Resident Evil ', 'Super Mario   ', 'Mortal Kombat ', 'Need For Speed', 'Street Fighter'
precos = '20,00 €', '19,90 €', '32,00 €', '25,00 €','28,00 €'

print('JOGOS ---------- PREÇO')
for c in range(0,5):
    print(f'{jogos[c]} - {precos[c]}')

