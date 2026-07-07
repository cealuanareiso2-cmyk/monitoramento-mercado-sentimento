from sqlalchemy import text
from database.connection import engine


def salvar_preco(preco):
    query = text("""
        INSERT INTO precos_ativos (
            ativo,
            preco,
            moeda,
            volume,
            data_preco
        )
        VALUES (
            :ativo,
            :preco,
            :moeda,
            :volume,
            :data_preco
        )
    """)

    with engine.begin() as connection:
        connection.execute(query, preco)