CREATE TABLE IF NOT EXISTS noticias (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    texto TEXT,
    fonte VARCHAR(100),
    url TEXT,
    ativo VARCHAR(20),
    sentimento VARCHAR(20),
    score_sentimento NUMERIC(10,4),
    data_publicacao TIMESTAMP,
    data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS precos_ativos (
    id SERIAL PRIMARY KEY,
    ativo VARCHAR(20) NOT NULL,
    preco NUMERIC(18,6),
    moeda VARCHAR(10),
    volume NUMERIC(18,2),
    variacao_percentual NUMERIC(10,4),
    data_preco TIMESTAMP,
    data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);