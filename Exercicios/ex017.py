# pedir ano de nasciumento e ano atual e calcular a idade do utilizador.

ano_nascimento = float(input('Em que ano você nasceu? '))
ano_atual = float(input('Em que ano estamos? '))

idade = ano_atual - ano_nascimento
print('A sua idade é',idade,'anos')
