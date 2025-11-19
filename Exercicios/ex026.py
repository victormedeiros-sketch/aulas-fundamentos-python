# Crie um programa que leia 5 notas de um aluno e calcule a sua média.
# >= 9.5 passou
# > 8 e < 9.5 em recuperação
# < 8 reprova

nota1 = float(input('Digite a primeira nota - '))
nota2 = float(input('Digite a segunda nota - '))
nota3 = float(input('Digite a terceira nota - '))
nota4 = float(input('Digite a quarta nota - '))
nota5 = float(input('Digite a quinta nota - '))

media = (nota1 + nota2 +nota3 + nota4 + nota5)/5

if media >= 9.5:
    print(f'Aprovado com uma média de {media:.2f}!')

elif media > 8:
    print(f'Em recuperação com uma média de {media:.2f}!')

else:
    print(f'Reprovado com uma média de {media:.2f}!')

