# Crie uma base de dados chamada loja.db e
# uma tabela chamada produtos com as
# seguintes colunas:
# id (INTEGER, PRIMARY KEY, autoincrement),
# nome (TEXT),
# preco (REAL),
# stock (INTEGER).

import sqlite3

def cabecalho(txt: str) -> None:
    print(f'---{txt}---')


def conectar():
    try:
        return sqlite3.connect('loja.db')
    except Exception as erro:
        print(f'Erro ao inciar ligação a base de dados: {str(erro)}')
        return ''


def tabela_produtos():
    conn = conectar()

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()



tabela_produtos()





