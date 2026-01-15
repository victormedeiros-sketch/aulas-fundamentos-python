# Insira 10 produtos fictícios na tabela
# criada anteriormente. Cada produto deve
# ter um nome, preço e quantidade de
# stock.
#
# Dica: Pode utilizar o executemany()

from ex086 import conectar



def inserir_produtos_iniciais():
    conn = conectar()
    if not conn:
        return

    cursor = conn.cursor()


    produtos = [
        ('Monitor 24"', 150.00, 10),
        ('Teclado Mecânico', 85.50, 20),
        ('Rato Gaming', 45.00, 15),
        ('Auscultadores', 120.00, 8),
        ('Tapete Mousepad XL', 25.00, 30),
        ('Webcam 1080p', 60.00, 12),
        ('Cabo HDMI 2m', 12.50, 50),
        ('Suporte Monitor', 35.00, 5),
        ('Pen Drive 64GB', 15.90, 40),
        ('Coluna Bluetooth', 55.00, 10)
    ]

    try:
        cursor.executemany('''
            INSERT INTO produtos (nome, preco, stock) 
            VALUES (?, ?, ?)
        ''', produtos)

        conn.commit()
        print(f'{len(produtos)} produtos inseridos com sucesso!')
    except Exception as e:
        print(f'Erro ao inserir dados: {e}')
    finally:
        conn.close()



inserir_produtos_iniciais()