# 5 numeros inteiros
# soma dos números

soma = 0 # a variavel soma vai mudadndo conforme o usuario vai digitando os números, ela começa com 0

for c in range(0,5): # incluiremos um contador para que eu não precise digitar a mesma frase 5 vezes
                     # contador c
                     # range de 0 a 5, ele vai levar esse contador a ser executado de 0 a 5


    numero = int(input(f'Digite o {c+1}º número inteiro: ')) # O número é escolhido pelo usuário e colocamos mais 1 para que
                                                                # a contagem comece no 1.

    soma += numero # soma que está em 0 recebe 0 + mumero
                         # na próxima volta que é a volta dois ele já terá um novo número em soma
                            # que foi atribuido pelo usuario, então nao é mais 0. agora é o numero atribuido + numero.


print(f' A soma dos numeros digitas é {soma}')





