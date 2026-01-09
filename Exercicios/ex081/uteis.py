def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        situacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        situacao = "Peso normal"
    elif 25.0 <= imc <= 29.9:
        situacao = "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        situacao = "Obesidade grau 1"
    elif 35.0 <= imc <= 39.9:
        situacao = "Obesidade grau 2"
    else:
        situacao = "Obesidade grau 3 (obesidade mórbida)"

    return imc, situacao


def guarda_txt(peso, altura, imc, situacao):
    with open('imc_relatorio.txt', 'a', encoding='utf-8') as file:
        file.write(f"Peso: {peso}kg | Altura: {altura}m | IMC: {imc:.2f} | Situação: {situacao}\n")
    print("Dados guardados com sucesso no ficheiro.")


