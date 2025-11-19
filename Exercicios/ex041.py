# Crie um programa que faça três perguntas ao utilizador
# A resposta só pode ser V ou F
# se estiver errado peça para repetir a resposta até ter um valor correto.



print('---RESPONDA V PARA VERDADEIRO E F PARA FALSO---')
while True:
    resposta = input('O cube tem seis faces? ').strip().upper()
    if resposta  == 'F':
        print('Errou')
    elif resposta == 'V':
        print('Acertou, vamos a próxima')
        break
    else:
        print('Resposta inválida.')


print('---RESPONDA V PARA VERDADEIRO E F PARA FALSO---')
while True:
    resposta = input('O ano tem 12 meses? ').strip().upper()
    if resposta  == 'F':
        print('Errou')
    elif resposta == 'V':
        print('Acertou, vamos a próxima')
        break
    else:
        print('Resposta inválida.')


print('---RESPONDA V PARA VERDADEIRO E F PARA FALSO---')
while True:
    resposta = input('O nome do formador é Ricardo? ').strip().upper()
    if resposta  == 'F':
        print('Errou')
    elif resposta == 'V':
        print('Acertou, fim')
        break
    else:
        print('Resposta inválida.')


