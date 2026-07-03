import requests
from config import NEWS_API_KEY, NEWS_PAGE_SIZE


def buscar_noticias(termo_busca):
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
        return None, response.status_code, response.text

    dados = response.json()
    return dados.get("articles", []), response.status_code, None