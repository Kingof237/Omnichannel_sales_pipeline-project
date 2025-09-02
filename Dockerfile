FROM apache/airflow:2.8.1-python3.11



# Install system dependencies for psycopg2-binary
USER root
RUN apt-get update && apt-get install -y git

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to airflow user
USER airflow

# Copy DAGs
COPY dags/ /opt/airflow/dags/

# Copy requirements
COPY requirements.txt .



# Install Python dependencies (Airflow already installed)
RUN pip install --no-cache-dir -r requirements.txt
=======
FROM apache/airflow:2.9.1-python3.11

WORKDIR /opt/airflow

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install dbt
RUN pip install dbt-core dbt-postgres

# Don’t copy DAGs here – they will be mounted via docker-compose
>>>>>>> 2ab5067631736bb00f03c20667a806258a294d52
