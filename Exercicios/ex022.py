# Crie um programa que leia o primeiro e último nome de uma pessoa e exiba as mensagens:
# “Olá nome, o seu registo está completo.”
# “O seu email é nome@empresa.pt” Ex email: Alfredo Xavier a.xavier@empresa.pt

from time import sleep

print('-_-_-_- SEJA BEM VINDO AO PROGRAMA _-_-_-_')
print('REGISTO DE UTILIZADOR: ')

nome = input('Nome: ').strip().lower()
sleep(1)
print(f'Olá {nome.title()}, o seu registo está completo.')

sleep(0.5)
print('A gerar o seu email...')
sleep(1)

p_nome = nome[0]
indice_espaco = nome.find(' ') + 1
u_nome = nome[indice_espaco:]
email = f'{p_nome}.{u_nome}@empresa.pt'
print(f'O seu email é {email}')
