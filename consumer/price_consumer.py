import json

from kafka import KafkaConsumer

from config import KAFKA_SERVER, TOPIC_PRICE
from database.price_repository import salvar_preco
from logger import logger


consumer = KafkaConsumer(
    TOPIC_PRICE,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="grupo-precos-db",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

logger.info("Consumer de preços iniciado. Aguardando mensagens...")


for mensagem in consumer:
    preco = mensagem.value

    salvar_preco(preco)

    logger.info(
        f"Preço salvo: {preco['ativo']} - {preco['preco']}"
    )