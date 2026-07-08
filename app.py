import subprocess
import sys
import time

processos = []

try:
    print("Iniciando Consumer de Notícias...")
    processos.append(
        subprocess.Popen([sys.executable, "-m", "consumer.kafka_consumer"])
    )

    time.sleep(2)

    print("Iniciando Consumer de Preços...")
    processos.append(
        subprocess.Popen([sys.executable, "-m", "consumer.price_consumer"])
    )

    time.sleep(2)

    print("Iniciando Scheduler...")
    processos.append(
        subprocess.Popen([sys.executable, "-m", "scheduler.scheduler"])
    )

    print("\nSistema iniciado com sucesso!")
    print("Pressione Ctrl + C para encerrar.\n")

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nEncerrando processos...")

    for processo in processos:
        processo.terminate()

    print("Sistema encerrado.")