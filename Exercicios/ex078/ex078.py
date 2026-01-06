# Crie um programa com uma função chamada
# fatorial(), que receba dois parâmetros:
# o primeiro será o número a calcular o
# fatorial e o segundo será opcional e
# lógico que indique se será exibido ou
# não o processo de cálculo do fatorial. O
# fatorial deve ser guardado num ficheiro
# txt.


def fatorial(numero: int, mostra=False) -> str:
    """
    -> Calculo de um numero com possibilidade de ver ym calculo
    :param numero: Número a ser usado para calcular o fatorial
    :param mostra:Opicional e boleada para True, ou false
    :return: string
    """
    from math import factorial
    fatorial_calculado = factorial(numero)

    if mostra: # if mostra == True | if not mostra == False
        while numero >= 1:
            if numero == 1:
                calculo += f'{numero} = '
            else:
                calculo += f'{numero} x '
                numero -= 1

    calculo += str(fatorial_calculado)

    return calculo


def guarda_txt(txt: str) -> None:
    from pathlib import Path

    caminho = Path(r'factorial.txt')

    with caminho.open('a')





