from config import ATIVOS_MONITORADOS
from logger import logger
from producer.news_api import buscar_noticias
from producer.kafka_producer import enviar_noticia


def coletar_e_enviar_noticias_para_kafka():
    total_enviadas = 0

    for termo_busca, ativo_codigo in ATIVOS_MONITORADOS.items():
        noticias, status_code, erro = buscar_noticias(termo_busca)

        if erro:
            logger.error(f"Erro na NewsAPI para {termo_busca}: {status_code} - {erro}")
            continue

        enviadas = 0

        for noticia in noticias:
            mensagem = {
                "titulo": noticia.get("title"),
                "texto": noticia.get("description"),
                "fonte": noticia.get("source", {}).get("name"),
                "url": noticia.get("url"),
                "ativo": ativo_codigo,
                "data_publicacao": noticia.get("publishedAt")
            }

            if not mensagem["url"]:
                continue

            enviar_noticia(mensagem)
            enviadas += 1

        total_enviadas += enviadas
        logger.info(f"{ativo_codigo}: {enviadas} notícias enviadas para Kafka.")

    logger.info(f"Coleta finalizada. Total enviado para Kafka: {total_enviadas}.")


