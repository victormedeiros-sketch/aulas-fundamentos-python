# Crie um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra “A”;
# Em que posição aparece a primeira vez;
# Em que posição aparece a última vez.

frase = input('Digige uma frase: ').strip()
print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)














