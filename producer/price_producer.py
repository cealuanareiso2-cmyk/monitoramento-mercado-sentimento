import yfinance as yf
from logger import logger
from producer.price_kafka_producer import enviar_preco


ATIVOS_YFINANCE = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "NVDA": "NVDA",
    "TSLA": "TSLA"
}


def coletar_e_enviar_precos_para_kafka():
    total_enviados = 0

    for ativo_codigo, ticker_codigo in ATIVOS_YFINANCE.items():
        ticker = yf.Ticker(ticker_codigo)
        dados = ticker.history(period="1d", interval="1m")

        if dados.empty:
            logger.warning(f"Nenhum preço encontrado para {ativo_codigo}")
            continue

        ultimo = dados.tail(1)

        mensagem = {
            "ativo": ativo_codigo,
            "preco": float(ultimo["Close"].iloc[0]),
            "moeda": "USD",
            "volume": float(ultimo["Volume"].iloc[0]),
            "abertura": float(ultimo["Open"].iloc[0]),
            "maxima": float(ultimo["High"].iloc[0]),
            "minima": float(ultimo["Low"].iloc[0]),
            "fechamento": float(ultimo["Close"].iloc[0]),
            "data_preco": ultimo.index[0].to_pydatetime().isoformat()
        }

        enviar_preco(mensagem)
        total_enviados += 1

        logger.info(f"{ativo_codigo}: preço enviado para Kafka.")

    logger.info(f"Coleta de preços finalizada. Total enviado: {total_enviados}.")