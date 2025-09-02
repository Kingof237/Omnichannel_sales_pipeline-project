import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import sys

sys.path.append("/opt/airflow/ETL")
import spotify
import walmart

local_tz = pendulum.timezone("UTC")

with DAG(
    dag_id="spotify_walmart_etl_dbt",
    start_date=pendulum.datetime(2025, 8, 19, tz=local_tz),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    tags=["spotify", "walmart", "dbt"]
) as dag:

    # Spotify ETL task
    run_spotify_etl = PythonOperator(
        task_id="spotify_etl",
        python_callable=spotify.main
    )

    # Walmart ETL task
    run_walmart_etl = PythonOperator(
        task_id="walmart_etl",
        python_callable=walmart.run_etl
    )

    # dbt deps task
    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command="cd /opt/airflow/dbt && dbt deps"
    )

    dbt_debug = BashOperator(
        task_id="dbt_debug",
        bash_command="cd /opt/airflow/dbt && dbt debug"
    )
    # dbt run task
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt && dbt run"
    )

    dbt_test= BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/dbt && dbt test"
    )

    # Define DAG order: Spotify → Walmart → dbt deps → dbt run
    run_spotify_etl >> run_walmart_etl >> dbt_deps >> dbt_debug >> dbt_run >> dbt_test