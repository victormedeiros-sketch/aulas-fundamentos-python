print('--------------TRIANGULO? SIM OU NÃO?------------')
print('Informe o comprimento de cada lado do triangulo:')
print('------------------------------------------------')
lado_a = float(input('Quantos cm tem o lado A? '))
lado_b = float(input('Quantos cm tem o lado B? '))
lado_c = float(input('Quantos cm tem o lado C? '))

if lado_a + lado_b > lado_c:
    print('É UM TRIANGULO!')
elif lado_a + lado_c > lado_b:
    print('É UM TRIANGULO!')
elif lado_b + lado_c > lado_a:
    print('É UM TRIANGULO!')
elif lado_c == lado_a == lado_b:
    print('É UM TRIANGULO!')
else:
    print('NÃO É UM TRIANGULO!')

