# Crie um simulador de crédito habitação
# simples e sem taxas, que solicite o nome,
# ano de nascimento, rendimentos mensais,
# despesas mensais, montante do crédito e
# prazo em anos, guardando tudo dentro de um
# dicionário. Calcule, acrescentando ao
# dicionário, a idade, o remanescente após
# despesas, quanto deverá pagar mensalmente
# pelo crédito e se o crédito foi aprovado
# sempre que o remanescente seja superior ao
# valor mensal do crédito.
from datetime import datetime
simulador = {}

print('--- SIMULAÇÃO DE CRÉDITO HABITAÇÃO ---')

simulador['Nome'] = input('Nome: \n--->')
simulador['Ano de nascimento'] = int(input('Ano de nascimento: \n--->'))
simulador['Rendimentos mensais'] = float(input('Rendimentos mensais: \n--->'))
simulador['Despesas mensais'] = float(input('Despesas mensais: \n--->'))
simulador['Montante do crédito'] = float(input('Montante do crédito: \n--->'))
simulador['Prazo de pagamento'] = int(input('Prazo de pagamento(em anos): \n--->'))

ano_atual = datetime.now().year

simulador['Remanescente'] = simulador['Rendimentos mensais'] - simulador['Despesas mensais']
simulador['Idade'] = ano_atual - simulador['Ano de nascimento']
simulador['Parcela'] = (simulador['Rendimentos mensais'] - simulador['Despesas mensais']) / 12 #corrigir

if simulador['Remanescente'] > simulador['Parcela']:
    simulador['Situação'] = 'Crédito aprovado'
else:
    simulador['Situação'] = 'Crédito negado'   #Refazer usando operador ternario

print(simulador)#completar com o do professor