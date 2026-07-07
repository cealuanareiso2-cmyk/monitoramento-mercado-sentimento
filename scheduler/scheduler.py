import time
import schedule

from producer.coletor_news import coletar_e_enviar_noticias_para_kafka
from producer.price_producer import coletar_e_enviar_precos_para_kafka
from logger import logger


def executar_pipeline():
    logger.info("Iniciando execução do pipeline...")

    coletar_e_enviar_noticias_para_kafka()
    coletar_e_enviar_precos_para_kafka()

    logger.info("Pipeline finalizado.")


# Para testes, vamos executar a cada 1 minuto.
# Depois podemos alterar para 5, 10 ou 15 minutos.
schedule.every(1).minutes.do(executar_pipeline)

logger.info("Scheduler iniciado.")

# Executa uma vez imediatamente
executar_pipeline()

while True:
    schedule.run_pending()
    time.sleep(1)