#Crie uma tuple preenchida com os 20 primeiros cocados da tabela do campeonato Brasileiro de futebol.
#Depois mostre:
#Os cinco primeiros colocados
#Os últimos 4 colocados
#Os times em ordem alfabetica
#Em que posição está o time do chapecoense

times =('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo',
        'Fluminense', 'Vasco da Gama', 'São Paulo', 'Red Bull Bragantino',
        'Corinthians', 'Grêmio', 'Ceará', 'Internacional', 'Atlético-MG',
        'Santos', 'Vitória', 'Chapecoense', 'Fortaleza', 'Sport')
print('Cinco primeiros colocados: ')
for indice, time in enumerate(times):
    if indice == 5:
        break
    else:
        print(f'\t{indice+1}º - {time}')

print('______________________________\n')

print('Quatro últimos colocados: ')
for indice, time in enumerate(times):
    if indice >= len(times) -4 :
        print(f'{indice}º\t{time}')

print('______________________________\n')

print('Times em ordem alfabética: ')
for time in sorted(times):
    print(f'\t',time)


print('______________________________\n')
print('Posição do time chapecoense:')

for indice, time in enumerate(times):
    esta_la = False
    indice_chapecoense = ''
    if indice == 'Chapecoense':
        esta_la = True
        print(f'A posição do time chapecoense é {indice}')
if esta_la:
    print(f'Chapeconse -> {indice_chapecoense + 1}º lugar')
else:
    print('Chapecoense não está classificado.')







