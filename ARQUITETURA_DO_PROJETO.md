# Arquitetura do Projeto

## Nome do Projeto

Monitoramento de Mercado e Sentimento

## Objetivo

Criar uma plataforma de Engenharia de Dados capaz de coletar notícias e preços de ativos financeiros, processar o sentimento dos textos e correlacionar essas informações com a variação dos preços em um dashboard.

## Fluxo Atual

NewsAPI → Python Collector → Análise de Sentimento → PostgreSQL

Yahoo Finance → Python Collector → PostgreSQL

## Arquitetura Final

NewsAPI → Kafka → Consumer → Sentiment Analysis → PostgreSQL → Data Warehouse → Power BI

Yahoo Finance → Kafka → Consumer → PostgreSQL → Data Warehouse → Power BI

## Tecnologias

- Python
- PostgreSQL
- SQLAlchemy
- NewsAPI
- Yahoo Finance
- VADER Sentiment
- Kafka
- Docker
- Airflow
- Power BI
- Git/GitHub

## Tabelas atuais

### noticias

Armazena notícias coletadas da NewsAPI.

Campos principais:

- titulo
- texto
- fonte
- url
- ativo
- sentimento
- score_sentimento
- data_publicacao
- data_coleta

### precos_ativos

Armazena preços coletados do Yahoo Finance.

Campos principais:

- ativo
- preco
- moeda
- volume
- variacao_percentual
- data_preco
- abertura
- maxima
- minima
- fechamento

## Próximos módulos

1. Evitar notícias duplicadas
2. Coletar múltiplos ativos
3. Criar coleta automática de preços
4. Adicionar Kafka
5. Criar producers e consumers
6. Criar Data Warehouse
7. Criar dashboard no Power BI
8. Documentar o TCC