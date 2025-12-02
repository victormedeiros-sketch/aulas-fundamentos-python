# importar o Pathlib
from pathlib import Path

#Criar a variavel que representa o caminho
caminho = Path(r'ficheiros/teste.txt')

with caminho.open('r', encoding='utf-8', errors='ignore') as file:
    for linha in file:
        print(linha, end='')