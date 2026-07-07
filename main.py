import sys

from producer.coletor_news import coletar_e_enviar_noticias_para_kafka
from producer.price_producer import coletar_e_enviar_precos_para_kafka


def main():
    if len(sys.argv) < 2:
        print("""
Uso:

python main.py noticias
python main.py precos
python main.py tudo
""")
        return

    comando = sys.argv[1].lower()

    if comando == "noticias":
        coletar_e_enviar_noticias_para_kafka()

    elif comando == "precos":
        coletar_e_enviar_precos_para_kafka()

    elif comando == "tudo":
        coletar_e_enviar_noticias_para_kafka()
        coletar_e_enviar_precos_para_kafka()

    else:
        print(f"Comando '{comando}' inválido.")


if __name__ == "__main__":
    main()