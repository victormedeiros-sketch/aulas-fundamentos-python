# Crie um programa com uma função que vai
# funcionar como a função input(), no
# entanto vai fazer a validação para
# aceitar apenas um valor numérico.

def input_numerico(txt):
    while True:
        valor = input(txt)
        try:
            return float(valor)
        except ValueError:
            print("Erro! Por favor, digite apenas números.")


num = input_numerico("Digite um valor numérico: ")
print(f"Valor aceito: {num}")