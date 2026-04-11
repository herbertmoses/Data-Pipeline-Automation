from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os
from store_to_postgres import store_to_postgres

# Add project path
sys.path.append("/Users/moses/PycharmProjects/automation_pipeline")

from join_tables_etl import run_etl
from folder_watcher import process_file

INPUT_DIR = "/Users/moses/automation_input"

def process_latest_file():
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]
    files.sort(reverse=True)

    if files:
        latest_file = os.path.join(INPUT_DIR, files[0])
        process_file(latest_file)


default_args = {
    "owner": "moses",
    "start_date": datetime(2026, 1, 1),
}

with DAG(
    "data_pipeline_dag",
    default_args=default_args,
    schedule="*/1 * * * *",  # every minute (test)
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    process_task = PythonOperator(
        task_id="process_data",
        python_callable=process_latest_file
    )

    store_task = PythonOperator(
        task_id="store_to_postgres",
        python_callable=store_to_postgres
    )

    etl_task >> process_task