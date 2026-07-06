from producer.kafka_producer import enviar_noticia

noticia = {
    "titulo": "Teste Kafka",
    "texto": "Primeira mensagem enviada para o Kafka.",
    "fonte": "Teste",
    "url": "https://teste-kafka.com/noticia-1",
    "ativo": "BTC"
}

enviar_noticia(noticia)

print("Mensagem enviada para o tópico noticias!")