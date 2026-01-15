# Altere os preços dos produtos com os ids
# 5, 6 e 7.

from ex086 import conectar, cabecalho


def atualizar_precos():
    cabecalho("ATUALIZANDO PREÇOS")

    conn = conectar()
    if not conn:
        return

    cursor = conn.cursor()


    alteracoes = [
        (99.90, 5),
        (120.00, 6),
        (15.00, 7)
    ]

    try:
        cursor.executemany('''
            UPDATE produtos 
            SET preco = ? 
            WHERE id = ?
        ''', alteracoes)

        conn.commit()
        print("Preços atualizados com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    atualizar_precos()