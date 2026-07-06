import json
from kafka import KafkaConsumer

from database.news_repository import salvar_noticia
from sentiment.analyzer import analisar_sentimento
from logger import logger


consumer = KafkaConsumer(
    "noticias",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="grupo-noticias-db",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)


logger.info("Consumer iniciado. Aguardando mensagens...")


for mensagem in consumer:
    noticia = mensagem.value

    titulo = noticia.get("titulo")
    texto = noticia.get("texto")
    fonte = noticia.get("fonte")
    url = noticia.get("url")
    ativo = noticia.get("ativo")
    data_publicacao = noticia.get("data_publicacao")

    texto_base = f"{titulo or ''} {texto or ''}"
    sentimento, score = analisar_sentimento(texto_base)

    resultado = salvar_noticia({
        "titulo": titulo,
        "texto": texto,
        "fonte": fonte,
        "url": url,
        "ativo": ativo,
        "sentimento": sentimento,
        "score_sentimento": score,
        "data_publicacao": data_publicacao
    })

    if resultado == 1:
        logger.info(f"Notícia salva no banco: {titulo}")
    else:
        logger.info(f"Notícia duplicada ignorada: {titulo}")