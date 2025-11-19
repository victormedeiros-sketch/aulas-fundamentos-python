# crie um programa que leia 4 valores e guarde-os numa tuple.
# quantas vezes aparece o numero 7?
# em que poição aparece o número 5?
# Quais são pares?
# O programa deve informar quando não encontrar resposta

# Leitura dos 4 valores e armazenamento na tuple
valores = (
    int(input('Digite o 1º número: ')),
    int(input('Digite o 2º número: ')),
    int(input('Digite o 3º número: ')),
    int(input('Digite o 4º número: '))
    )

print(f'\nVocê digitou os valores: {valores}')
print('-' * 30)

qtd_setes = valores.count(7)

if qtd_setes > 0:
    print(f'O número 7 apareceu {qtd_setes} vezes.')
else:
    print('O número 7 não foi digitado.')

try:
    indice_cinco = valores.index(5)
    print(f'O número 5 foi digitado na {indice_cinco + 1}ª posição.')
except ValueError:
    print('O número 5 não foi encontrado em nenhuma posição.')

print('\nOs valores pares digitados foram:')
pares_encontrados = False
for numero in valores:
    if numero % 2 == 0:
        print(numero, end=' ')
        pares_encontrados = True

if not pares_encontrados:
    print('Nenhum número par foi digitado.')
else:
    print('')

print('-' * 30)