print('---CALCULADORA IMC---')

altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Com um IMC de {imc:.2f} a sua classificação é: Abaixo do peso.')
elif imc < 24.9:
    print(f'Com um IMC de {imc:.2f} a sua classificação é: Peso normal.')
elif imc < 29.9:
    print(f'Com um IMC de {imc:.2f} a sua classificação é: Sobrepeso.')
elif imc < 34.9:
    print(f'Com um IMC de {imc:.2f} a sua classificação é: Obesidade grau 1.')
elif imc < 39.9:
    print(f'Com um IMC de {imc:.2f} a sua classificação é: Obesidade grau 2.')
else:
    print(f'Com um IMC de {imc:.2f} a sua classificação é: Obesidade grau 3.')


