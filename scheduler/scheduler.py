import time
import schedule

from config import INTERVALO_MINUTOS
from logger import logger
from producer.coletor_news import coletar_e_enviar_noticias_para_kafka
from producer.price_producer import coletar_e_enviar_precos_para_kafka


def executar_pipeline():
    logger.info("Iniciando execução do pipeline...")

    try:
        coletar_e_enviar_noticias_para_kafka()
        coletar_e_enviar_precos_para_kafka()

        logger.info("Pipeline finalizado com sucesso.")

    except Exception as e:
        logger.exception(f"Erro durante a execução do pipeline: {e}")


schedule.every(INTERVALO_MINUTOS).minutes.do(executar_pipeline)

logger.info(
    f"Scheduler iniciado. Execução a cada {INTERVALO_MINUTOS} minuto(s)."
)

# Primeira execução imediatamente
executar_pipeline()

while True:
    schedule.run_pending()
    time.sleep(1)