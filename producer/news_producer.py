from database.connection import engine
from sqlalchemy import text

def inserir_noticia_teste():
    query = text("""
        INSERT INTO noticias (
            titulo, texto, fonte, url, ativo,
            sentimento, score_sentimento, data_publicacao
        )
        VALUES (
            'Bitcoin sobe após otimismo do mercado',
            'Investidores demonstram confiança no Bitcoin após alta no volume de negociações.',
            'Teste Manual',
            'https://exemplo.com/noticia-bitcoin',
            'BTC',
            'positivo',
            0.75,
            CURRENT_TIMESTAMP
        )
    """)

    with engine.begin() as connection:
        connection.execute(query)

    print("Notícia teste inserida com sucesso!")