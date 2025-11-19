#PERGUNTAR O SALÁRIO
#SALÁRIOS SUPERIORES A 1250 AUMENTO DE 10%
#SALÁRIOS INFERIORES OU IGUAIS AUMENTO DE 15%

print('---Aumento de salários---')
print('Qual o seu salário atua? ')
salario = float(input('(€)--->'))

if salario <= 1250.00:
    print(f'O seu novo salário é {salario + ((salario / 100) * 15)}€')
else:
    print(f'O seu novo salário é {salario + ((salario / 100) * 10)}€')


