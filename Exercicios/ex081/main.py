import uteis

p = float(input("Digite o seu peso (kg): "))
a = float(input("Digite a sua altura (m): "))


valor_imc, classe = uteis.calcular_imc(p, a)


print(f"Resultado: {valor_imc:.2f} - {classe}")


uteis.guarda_txt(p, a, valor_imc, classe)