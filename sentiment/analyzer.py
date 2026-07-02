from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analisador = SentimentIntensityAnalyzer()

def analisar_sentimento(texto):
    if texto is None:
        texto = ""

    resultado = analisador.polarity_scores(texto)
    score = resultado["compound"]

    if score >= 0.05:
        sentimento = "positivo"
    elif score <= -0.05:
        sentimento = "negativo"
    else:
        sentimento = "neutro"

    return sentimento, score