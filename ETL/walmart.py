import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_etl():
    dataset = os.getenv("KAGGLE_DATASET", "ankitrajmishra/walmart")
    download_path = "data"
    os.makedirs(download_path, exist_ok=True)

    # Kaggle authentication
    api = KaggleApi()
    api.authenticate()  # reads KAGGLE_CONFIG_DIR automatically

    logger.info("📥 Downloading dataset from Kaggle...")
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    logger.info("✅ Download complete.")

    file_path = os.path.join(download_path, "Walmart.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    df = pd.read_csv(file_path)
    logger.info(f"📊 Loaded {len(df)} records")

    # Postgres credentials from env
    user = os.getenv("PG_USER")
    password = quote_plus(os.getenv("PG_PASSWORD"))
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    database = os.getenv("PG_DATABASE")
    schema = os.getenv("PG_SCHEMA")
    table_name = os.getenv("PG_TABLE")

    if not all([user, password, host, port, database, schema, table_name]):
        raise ValueError("Postgres environment variables not fully set")

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

    with engine.begin() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
        df.to_sql(table_name, conn, if_exists="replace", index=False, schema=schema)
        logger.info(f"✅ Data saved to {schema}.{table_name}")

    return df

if __name__ == "__main__":
    run_etl()
