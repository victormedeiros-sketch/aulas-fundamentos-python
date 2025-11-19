lanche = ('Hamburguer', 'Chocolate', 'Pudim')
jantar = ('frago','macarrão','Hamburguer')
comidas = lanche + jantar


'''print(comidas.index('Hamburguer',1))''' # ele devolve a posição do primeiro hamburguer que é 0.
                                            # o virgula 1 é para mostrar a próxima depois da posição 0

'''print(lanche.index('Pudim'))''' #Mostra a posição do elemento, o indice em que el se encontra.

'''print(lanche.count('Chocolate'))''' #Conta quantas vezes aparece o elemento

'''print(sorted(lanche))''' #Coloca em ordem

'''for comida in lanche:                       #se precisar mostrar a posuição usando esse. 
                                                 #Precisa colocar o e numerate depois do in e usar duas variáveis 
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')'''

#ou

'''for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posiçãol {c}') #Se precisar mostrar a posição é mais facil usar nesse

#As duas maneiras dão certo! Depende de cada caso precisar de uma ou de outra'''