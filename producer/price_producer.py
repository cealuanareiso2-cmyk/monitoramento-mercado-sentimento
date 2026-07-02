import yfinance as yf
from sqlalchemy import text
from database.connection import engine


def coletar_preco_bitcoin():

    ticker = yf.Ticker("BTC-USD")

    dados = ticker.history(
        period="1d",
        interval="1m"
    )

    if dados.empty:
        print("Nenhum dado encontrado.")
        return

    ultimo = dados.tail(1)

    abertura = float(ultimo["Open"].iloc[0])
    maxima = float(ultimo["High"].iloc[0])
    minima = float(ultimo["Low"].iloc[0])
    fechamento = float(ultimo["Close"].iloc[0])

    volume = float(ultimo["Volume"].iloc[0])

    data_preco = ultimo.index[0].to_pydatetime()

    query = text("""
        INSERT INTO precos_ativos (
            ativo,
            preco,
            moeda,
            volume,
            variacao_percentual,
            data_preco,
            abertura,
            maxima,
            minima,
            fechamento
        )

        VALUES (

            :ativo,
            :preco,
            :moeda,
            :volume,
            :variacao,
            :data_preco,
            :abertura,
            :maxima,
            :minima,
            :fechamento

        )
    """)

    with engine.begin() as connection:

        connection.execute(query, {

            "ativo": "BTC",

            "preco": fechamento,

            "moeda": "USD",

            "volume": volume,

            "variacao": 0,

            "data_preco": data_preco,

            "abertura": abertura,

            "maxima": maxima,

            "minima": minima,

            "fechamento": fechamento

        })

    print("\nPreço salvo com sucesso!\n")

    print(f"Abertura   : {abertura}")
    print(f"Máxima     : {maxima}")
    print(f"Mínima     : {minima}")
    print(f"Fechamento : {fechamento}")
    print(f"Volume     : {volume}")