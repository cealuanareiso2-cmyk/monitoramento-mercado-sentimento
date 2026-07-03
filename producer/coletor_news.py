import requests
from sqlalchemy import text

from database.connection import engine
from sentiment.analyzer import analisar_sentimento
from logger import logger
from config import NEWS_API_KEY, NEWS_PAGE_SIZE, ATIVOS_MONITORADOS


def coletar_e_salvar_noticias():
    total_inseridas = 0
    total_duplicadas = 0

    for termo_busca, ativo_codigo in ATIVOS_MONITORADOS.items():
        url = (
            "https://newsapi.org/v2/everything?"
            f"q={termo_busca}&"
            "language=pt&"
            "sortBy=publishedAt&"
            f"pageSize={NEWS_PAGE_SIZE}&"
            f"apiKey={NEWS_API_KEY}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            logger.error(f"Erro na NewsAPI para {termo_busca}: {response.status_code} - {response.text}")
            continue

        dados = response.json()
        noticias = dados.get("articles", [])

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


