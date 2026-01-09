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


def adicionar_produtos():
    cabecalho('ADICIONAR PRODUTO')
    nome_produto = input('Nome do produto a ser adicionado: ').strip()
    preco_produto = float(input('Preço(€): '))
    stock_produto = int(input('Quantidade de itens a adicionar: '))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO produtos(nome, preco, stock) VALUES(?,?,?)",(nome_produto, preco_produto, stock_produto))
    conn.commit()
    conn.close()
    input(f'"{nome_produto}" adicionado com sucesso!')


def mostrar_produtos():
    cabecalho('STOCK DA LOJA')
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    for produto in produtos:
        print('--------------------------------------------------------------')
        print(f'ID: {produto[0]} | NOME {produto[1]} | PREÇO: {produto[2]} | STOCK: {produto[3]}')

        input()


def exluir_produto():
    cabecalho('EXCLUIR PRODUTO')
    id_produto = input('Digite o ID do produto para excluir: ')

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

    conn.commit()
    conn.close()

    print('Produto exluido com sucesso.')


def alterar_stock():
    cabecalho('ALTERAR STOCK ')
    id_produto = input('Digite o ID do produto para editar a quantidade de produtos em stock: ')
    nova_qtd = int(input('Digite a quantidade correta de produtos em stock: '))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE produtos SET stock_produto = ? WHERE id = ?", (nova_qtd, id_produto))

    conn.commit()
    conn.close()

    print('Stock atualizado com sucesso.')


def menu():
    tabela_produtos()
    while True:
        print('[ 1 ] - Adicionar Produto')
        print('[ 2 ] - Mostrar Produtos')
        print('[ 3 ] - Exluir Produtos')
        print('[ 4 ] - Alterar Stock')
        print('[ 5 ] - Sair')
        opcao = input('---> ')

        match opcao:
            case '1':
                adicionar_produtos()
            case '2':
                mostrar_produtos()
            case '3':
                exluir_produto()
            case '4':
                alterar_stock()
            case '5':
                break
            case _:
                print('Opção inválida.')



if __name__ == '__main__':
    menu()







