from sqlalchemy import create_engine

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
from logger import logger


DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


def test_connection():
    try:
        with engine.connect():
            logger.info("Conexão com PostgreSQL realizada com sucesso!")
    except Exception as e:
        logger.error(f"Erro ao conectar no PostgreSQL: {e}")