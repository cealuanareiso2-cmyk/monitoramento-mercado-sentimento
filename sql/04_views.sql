DROP VIEW IF EXISTS vw_dashboard_mercado;

CREATE VIEW vw_dashboard_mercado AS

WITH ultimo_preco AS (

    SELECT DISTINCT ON (ativo)
        ativo,
        preco,
        abertura,
        maxima,
        minima,
        fechamento,
        variacao_percentual,
        volume,
        moeda,
        data_preco
    FROM precos_ativos
    ORDER BY ativo, data_preco DESC

)

SELECT

    n.id AS noticia_id,

    n.ativo,

    n.titulo,

    n.texto,

    n.fonte,

    n.url,

    n.sentimento,

    n.score_sentimento,

    CASE
        WHEN n.score_sentimento >= 0.20 THEN 'Positivo'
        WHEN n.score_sentimento <= -0.20 THEN 'Negativo'
        ELSE 'Neutro'
    END AS categoria_sentimento,

    n.data_publicacao,

    n.data_coleta,

    EXTRACT(YEAR FROM n.data_publicacao) AS ano,

    EXTRACT(MONTH FROM n.data_publicacao) AS mes,

    EXTRACT(DAY FROM n.data_publicacao) AS dia,

    TO_CHAR(n.data_publicacao,'Month') AS nome_mes,

    up.preco,

    up.abertura,

    up.maxima,

    up.minima,

    up.fechamento,

    up.variacao_percentual,

    up.volume,

    up.moeda,

    up.data_preco

FROM noticias n

LEFT JOIN ultimo_preco up
ON up.ativo = n.ativo;