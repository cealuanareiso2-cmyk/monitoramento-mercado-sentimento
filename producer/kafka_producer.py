import json

from kafka import KafkaProducer

from config import KAFKA_SERVER, TOPIC_NEWS


producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def enviar_noticia(noticia):
    producer.send(TOPIC_NEWS, noticia)
    producer.flush()