from sqlalchemy import text

from config import ATIVOS_MONITORADOS
from database.connection import engine
from sentiment.analyzer import analisar_sentimento
from logger import logger
from producer.news_api import buscar_noticias


def coletar_e_salvar_noticias():
    total_inseridas = 0
    total_duplicadas = 0

    for termo_busca, ativo_codigo in ATIVOS_MONITORADOS.items():
        noticias, status_code, erro = buscar_noticias(termo_busca)

        if erro:
            logger.error(f"Erro na NewsAPI para {termo_busca}: {status_code} - {erro}")
            continue

        inseridas = 0
        duplicadas = 0

        for noticia in noticias:
            titulo = noticia.get("title")
            texto = noticia.get("description")
            fonte = noticia.get("source", {}).get("name")
            url_noticia = noticia.get("url")
            data_publicacao = noticia.get("publishedAt")

            if not url_noticia:
                continue

            texto_base = f"{titulo or ''} {texto or ''}"
            sentimento, score = analisar_sentimento(texto_base)

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
                result = connection.execute(query, {
                    "titulo": titulo,
                    "texto": texto,
                    "fonte": fonte,
                    "url": url_noticia,
                    "ativo": ativo_codigo,
                    "sentimento": sentimento,
                    "score_sentimento": score,
                    "data_publicacao": data_publicacao
                })

            if result.rowcount == 1:
                inseridas += 1
            else:
                duplicadas += 1

        total_inseridas += inseridas
        total_duplicadas += duplicadas

        logger.info(f"{ativo_codigo}: inseridas {inseridas}, duplicadas {duplicadas}")

    logger.info(f"Coleta finalizada. Total inseridas: {total_inseridas}. Total duplicadas: {total_duplicadas}.")


