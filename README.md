# 📊 Monitoramento de Mercado e Análise de Sentimento

Projeto de Engenharia de Dados desenvolvido para monitorar notícias e preços de ativos financeiros em tempo real, utilizando um pipeline de ingestão, processamento e visualização de dados.

---

## 🎯 Objetivo

Desenvolver uma solução completa de Engenharia de Dados capaz de:

- Capturar notícias relacionadas ao mercado financeiro.
- Coletar preços de criptomoedas e ações.
- Processar e classificar o sentimento das notícias.
- Armazenar os dados em um banco PostgreSQL.
- Disponibilizar indicadores em um dashboard interativo no Power BI.

---

## 🛠 Tecnologias Utilizadas

- Python
- Apache Kafka
- PostgreSQL
- Docker
- Power BI
- SQLAlchemy
- NewsAPI
- Yahoo Finance (yfinance)
- NLP (TextBlob)
- Schedule
- Git e GitHub

---

## 🏗 Arquitetura

```text
                NewsAPI
                   │
                   │
                   ▼
              Producer Python
                   │
                   ▼
               Apache Kafka
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
Consumer Notícias      Consumer Preços
        │                     │
        └──────────┬──────────┘
                   ▼
              PostgreSQL
                   │
                   ▼
            View Analítica
                   │
                   ▼
              Power BI
```

---

## 📂 Estrutura do Projeto

```text
monitoramento-mercado-sentimento/
│
├── consumer/
├── producer/
├── database/
├── scheduler/
├── sentiment/
├── dashboard/
├── sql/
├── data/
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Funcionalidades

- ✅ Coleta automática de notícias.
- ✅ Coleta automática de preços.
- ✅ Pipeline de dados com Kafka.
- ✅ Processamento de sentimento.
- ✅ Armazenamento em PostgreSQL.
- ✅ Dashboard em Power BI.
- ✅ Scheduler para execução automática.
- ✅ Configuração via variáveis de ambiente.

---

## 📈 Dashboard

O dashboard apresenta:

- 📰 Total de notícias coletadas.
- 📈 Ativos monitorados.
- 💰 Último preço de BTC, ETH, NVDA e TSLA.
- 😊 Distribuição dos sentimentos.
- 📊 Notícias por ativo.
- 📈 Evolução dos preços.

*(Adicione aqui uma imagem do dashboard quando publicar o projeto.)*

---

## 🚀 Como executar

### Clone o projeto

```bash
git clone https://github.com/SEU-USUARIO/monitoramento-mercado-sentimento.git
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Configure o arquivo `.env`

Utilize o arquivo `.env.example` como base.

### Suba os containers

```bash
docker compose up -d
```

### Execute os consumers

```bash
python -m consumer.kafka_consumer
python -m consumer.price_consumer
```

### Execute o scheduler

```bash
python -m scheduler.scheduler
```

---

## 🎓 Objetivos de aprendizado

Este projeto foi desenvolvido para praticar:

- Engenharia de Dados
- ETL
- Streaming de Dados
- Apache Kafka
- PostgreSQL
- Docker
- Power BI
- Integração com APIs
- Versionamento com Git

---

## 👩‍💻 Autora

**Luana dos Reis**

LinkedIn: *([https://www.linkedin.com/in/luana-reis-53552626a/])*

GitHub: *(https://github.com/cealuanareiso2-cmyk)*