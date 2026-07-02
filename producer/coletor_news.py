import os
import requests
from dotenv import load_dotenv
from sqlalchemy import text
from database.connection import engine
from sentiment.analyzer import analisar_sentimento

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def coletar_e_salvar_noticias():
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=bitcoin&"
        f"language=pt&"
        f"sortBy=publishedAt&"
        f"pageSize=10&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)
    dados = response.json()

    for noticia in dados["articles"]:
        texto_base = f"{noticia['title']} {noticia['description']}"
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
        """)

        with engine.begin() as connection:
            connection.execute(query, {
                "titulo": noticia["title"],
                "texto": noticia["description"],
                "fonte": noticia["source"]["name"],
                "url": noticia["url"],
                "ativo": "BTC",
                "sentimento": sentimento,
                "score_sentimento": score,
                "data_publicacao": noticia["publishedAt"]
            })

    print("Notícias com sentimento salvas no PostgreSQL!")


coletar_e_salvar_noticias()