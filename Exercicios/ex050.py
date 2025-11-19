# Ler idade e sexo de varias pessoas
# A cada pessoa registada o programa pergunta se quer continuar ou não
# Mostrar quantas pessoas tem mais de 25 anos
# Mostrar quantos homens com mais de 17 foram registados
# Mostrar quantas mulheres foram registadas
# Mostrar quantos menores de idade foram registados

pessoas_mais25 = 0
homens_menos17 = 0
mulheres = 0
menores = 0

resposta = ''
idade = ''
sexo = ''

while resposta != 'nao':
    idade = int(input('Digite a idade: '))
    if idade < 0:
        print('Por favor isira uma idade valida')
        continue

    while True:
     sexo = input('Digite o sexo M/F: ').strip().lower()
     if sexo != 'm' or sexo != 'f':

        resposta = input('Deseja continuar? [sim / não]')
        break

    if idade > 25:
        pessoas_mais25 += 1

    if sexo == 'm' and idade < 17:
        homens_menos17 += 1

    if sexo == 'f':
        mulheres += 1

    if idade < 18:
            menores += 1



print(f'{pessoas_mais25} das pessoas registadas tem mais de 25 anos.')
print(f'{homens_menos17} homens tem menos de 17 anos.')
print(f'{mulheres} são mulheres.')
print(f'{menores} das pessoas registadas são menores de idade.')
