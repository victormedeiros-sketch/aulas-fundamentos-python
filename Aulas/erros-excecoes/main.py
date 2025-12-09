try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))


    print(f'{num1} / {num2} = {num1 / num2}')

except ZeroDivisionError:
    print('Não é possivel dividir por zero')

except KeyboardInterrupt:
    print('O utilizador encerrou o programa')

except ValueError:
    print('Por favor digite um número válido')

else:
    print(f'{num1} / {num2} = {num1 / num2}')

finally:
    print('Programa encerrado')


'''except:
    print('Ops! Ocorreu um erro.')'''

'''except Exception as e:
    print(e)'''