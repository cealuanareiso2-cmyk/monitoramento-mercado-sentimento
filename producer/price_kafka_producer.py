import json

from kafka import KafkaProducer

from config import KAFKA_SERVER, TOPIC_PRICE


producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def enviar_preco(preco):
    producer.send(TOPIC_PRICE, preco)
    producer.flush()