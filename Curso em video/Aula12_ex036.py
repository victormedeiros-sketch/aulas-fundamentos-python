# Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa
# o program vai perguntar:
# valor da casa
# salario
# em quantos anos vai pagar
# Calcular o valor da parcela mensal sabendo que ela não pode exceder 30% do salario, se exceder será negado o empréstimo

print(('='*10),'Banco Portugal',('='*10))
print('_'*36)
print('Simulação de empréstimo')
print('_'*36)

print('Valor do imóvel:')
v_imovel = float(input('---> '))

print('Renda mensal: ')
renda = float(input('---> '))

print('Em quantos anos pretende pagar? ')
tempo_pgto = int(input('---> '))

v_parcela = v_imovel / (tempo_pgto * 12)

if v_parcela <= renda - ((renda/100)*30):
    print('Financiamento aprovado!')
    print(f'{tempo_pgto * 12} parcelas de {v_parcela}€')
else:
    print('Financiamento negado. O valor da parcela excede 30% da sua renda mensal')

