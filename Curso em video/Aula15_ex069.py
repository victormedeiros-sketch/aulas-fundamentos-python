# Programa que leia a idade e sexo de várias pessoas
# A cada rodada o programa deve perguntar se o usúario quer continuar
# no final mostre quantas pessoas tem mais de 18 anos
# quantos homons foram cadastrados
# quantas mulheres tem mais de 20 anos

mais_18 = 0
homens = 0
m_20 = 0

while True:
    print('_' * 20)
    print('FICHA DE CADASTRO')
    print('_'*20)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M / F]: ').upper().strip()

    if idade > 18:
        mais_18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade > 20:
        m_20 += 1

    print('_' * 20)
    print('[1] - Continuar')
    print('[2] - Finalizar')
    ct = int(input('--->'))

    if ct == 2:
        break


print(f'{mais_18} das pessoas cadastradas tem mais de 18 anos.')
print(f'{homens} das pessoas cadastradas são homens')
print(f'{m_20} das mulheres caastradas tem mais de 20 anos')