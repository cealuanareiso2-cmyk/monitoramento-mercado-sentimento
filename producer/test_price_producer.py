from producer.price_kafka_producer import enviar_preco

preco = {
    "ativo": "BTC",
    "preco": 62000.15,
    "moeda": "USD",
    "volume": 1548752,
    "data_preco": "2026-07-07T13:30:00"
}

enviar_preco(preco)

print("Preço enviado para o tópico precos!")