# Omnichannel Sales Pipeline  

This project implements an **end-to-end data pipeline** for omnichannel sales analytics, integrating data from multiple sources (Walmart, Spotify, and Kaggle datasets) using **dbt**, **Airflow**, and **Docker**.  

It provides a unified analytics-ready warehouse that supports **reporting, forecasting, and decision-making**.  

---

## 📂 Project Structure  

- **Omnichannel_Sales_Pipeline/**
  - **.vscode/**
  - **dags/**
  - **dbt/**
    - analyses/
    - data/
    - dbt_internal_packages/
    - dbt_packages/
    - logs/
    - macros/
    - models/
    - seeds/
    - snapshots/
    - target/
    - tests/
    - dbt_project.yml
    - package-lock.yml
    - packages.yml
    - profiles.yml
    - README.md
  - **ETL/**
    - spotify.py
    - walmart.py
    - __init__.py
  - **kaggle/**
    - kaggle.json
  - **venv/**
    - Include/
    - Lib/
    - Scripts/
    - share/
    - pyvenv.cfg
  - **airflow/**
    - .airflowignore
    - airflow.cfg
    - dag.py
    - __pycache__/
  - **data/**
  - .env
  - .env.example
  - .gitignore
  - docker-compose.yml
  - Dockerfile
  - init.sql
  - requirements.txt
  - settings.json
  - README.md

---

## ⚙️ Tech Stack  

- **Airflow** → DAG orchestration  
- **dbt** → Data transformations, modeling, testing  
- **Docker & docker-compose** → Containerized environment  
- **Postgres** (or your chosen warehouse) → Data storage  
- **Kaggle API** → External datasets integration  
- **Python** → ETL scripts and automation  

---

## 🚀 Getting Started  

1. **Clone the repo**
    ```bash
    git clone https://github.com/Kingof237/Omnichannel_Sales_Pipeline.git
    cd Omnichannel_Sales_Pipeline
    ```

2. **Setup environment**
    - Create a Python virtual environment:
      ```bash
      python -m venv venv
      ```
    - Activate the environment:
      - Windows:
        ```bash
        venv\Scripts\activate
        ```
      - Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
    - Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```

3. **Setup environment variables**
    - Copy `.env.example` to `.env`
    - Update credentials and paths as needed

4. **Run with Docker**
    ```bash
    docker-compose up --build
    ```

5. **Initialize dbt**
    - Install dbt dependencies:
      ```bash
      dbt deps
      ```
    - Seed static data:
      ```bash
      dbt seed
      ```
    - Run dbt models:
      ```bash
      dbt run
      ```
    - Run dbt tests:
      ```bash
      dbt test
      ```

---

## ✅ Features  
- Unified data ingestion from Walmart, Spotify, and Kaggle  
- Cleaned & standardized **dbt models** for analytics  
- **Incremental dbt models** for scalable transformations  
- **Data quality tests** (dbt tests)  
- **Airflow DAGs** to automate ETL + dbt runs  
- **Dockerized setup** for reproducibility  

---

## 📌 Next Steps  
- Add CI/CD with GitHub Actions  
- Integrate BI dashboard (Metabase / Looker / Power BI)  
- Add forecasting models  

---

## 👨‍💻 Author  
Built by **Kingof237** 🚀  
