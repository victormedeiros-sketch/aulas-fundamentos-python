# Crie uma Interface Simples no Terminal
# para Gestão de Produtos.
# O programa deve permitir:
# Adicionar novos produtos (com nome, preço e
# stock),
# Mostrar todos os produtos da base de dados,
# Alterar um produto existente (nome, preço ou
# stock).
from ex086 import conectar, cabecalho, tabela_produtos

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
        print('[ 3 ] - Alterar Stock')
        print('[ 4 ] - Sair')
        opcao = input('---> ')

        match opcao:
            case '1':
                adicionar_produtos()
            case '2':
                mostrar_produtos()
            case '3':
                alterar_stock()
            case '4':
                break
            case _:
                print('Opção inválida.')



if __name__ == '__main__':
    menu()