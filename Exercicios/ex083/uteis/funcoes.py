def titulo(txt: str) -> None:
    tamanho = len(txt) + 4
    print('_'* tamanho)
    print(f'  {txt}')
    print('_'* tamanho)



def obter_numero(txt: str) -> float:
    while True:
        try:
            return float(input(txt))
        except ValueError:
            print('Erro: Entrada inválida. Digite apenas números.')


def dividir(a: float, b: float) -> None:
    if b == 0:
        print('Erro: Não é possível dividir por zero!')
    else:
        resultado = a / b
        print(f'O resultado da divisão é: {resultado:.2f}')


