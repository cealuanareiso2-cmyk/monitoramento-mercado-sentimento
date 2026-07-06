from sqlalchemy import text
from database.connection import engine


def salvar_noticia(noticia):
    query = text("""
        INSERT INTO noticias (
            titulo, texto, fonte, url, ativo,
            sentimento, score_sentimento, data_publicacao
        )
        VALUES (
            :titulo, :texto, :fonte, :url, :ativo,
            :sentimento, :score_sentimento, :data_publicacao
        )
        ON CONFLICT (url) DO NOTHING
    """)

    with engine.begin() as connection:
        result = connection.execute(query, noticia)

    return result.rowcount