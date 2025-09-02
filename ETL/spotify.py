import os
import io
import pandas as pd
import requests
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_mockaroo_data():
    api_key = os.getenv("MOCKAROO_API_KEY")
    schema_id = os.getenv("MOCKAROO_SCHEMA_ID")
    num_rows = int(os.getenv("MOCKAROO_NUM_ROWS", "1000"))

    if not api_key or not schema_id:
        raise ValueError("MOCKAROO_API_KEY or MOCKAROO_SCHEMA_ID not set in environment")

    url = f"https://api.mockaroo.com/api/{schema_id}?count={num_rows}"
    headers = {"X-API-Key": api_key}

    logger.info(f"Fetching data from Mockaroo: {url}")
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    df = pd.read_csv(io.StringIO(response.text))
    logger.info(f"✅ Fetched {len(df)} rows from Mockaroo")
    return df

def load_to_postgres(df):
    user = os.getenv("PG_USER")
    password = quote_plus(os.getenv("PG_PASSWORD"))
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    database = os.getenv("PG_DATABASE")
    schema = os.getenv("PG_SCHEMA")
    table_name = os.getenv("PG_TABLE1")

    if not all([user, password, host, port, database, schema, table_name]):
        raise ValueError("Postgres environment variables not fully set")

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

    with engine.begin() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
        df.to_sql(table_name, conn, if_exists="replace", index=False, schema=schema)
        logger.info(f"✅ Data saved to {schema}.{table_name}")

def main():
    df = fetch_mockaroo_data()
    load_to_postgres(df)

if __name__ == "__main__":
    main()
