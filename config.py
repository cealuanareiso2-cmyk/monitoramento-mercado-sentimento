import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# BANCO
# ==========================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# ==========================
# APIS
# ==========================

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# ==========================
# NEWS API
# ==========================

NEWS_LANGUAGE = "pt"

NEWS_PAGE_SIZE = 10


ATIVOS_MONITORADOS = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "nvidia": "NVDA",
    "tesla": "TSLA"
}


CRIPTO_ATIVOS = [
    "bitcoin",
    "ethereum"
]

ACOES = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA"
]