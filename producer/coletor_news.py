import requests
from sqlalchemy import text

from database.connection import engine
from sentiment.analyzer import analisar_sentimento
from logger import logger
from config import NEWS_API_KEY, NEWS_PAGE_SIZE


def coletar_e_salvar_noticias():
    url = (
        "https://newsapi.org/v2/everything?"
        "q=bitcoin&"
        "language=pt&"
        "sortBy=publishedAt&"
        f"pageSize={NEWS_PAGE_SIZE}&"
        f"apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        logger.error(f"Erro na NewsAPI: {response.status_code} - {response.text}")
        return

    dados = response.json()
    noticias = dados.get("articles", [])

    if not noticias:
        logger.warning("Nenhuma notícia encontrada.")
        return

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
                titulo,
                texto,
                fonte,
                url,
                ativo,
                sentimento,
                score_sentimento,
                data_publicacao
            )
            VALUES (
                :titulo,
                :texto,
                :fonte,
                :url,
                :ativo,
                :sentimento,
                :score_sentimento,
                :data_publicacao
            )
            ON CONFLICT (url) DO NOTHING
        """)

        with engine.begin() as connection:
            result = connection.execute(query, {
                "titulo": titulo,
                "texto": texto,
                "fonte": fonte,
                "url": url_noticia,
                "ativo": "BTC",
                "sentimento": sentimento,
                "score_sentimento": score,
                "data_publicacao": data_publicacao
            })

        if result.rowcount == 1:
            inseridas += 1
        else:
            duplicadas += 1

    logger.info(f"Coleta finalizada. Inseridas: {inseridas}. Duplicadas ignoradas: {duplicadas}.")


