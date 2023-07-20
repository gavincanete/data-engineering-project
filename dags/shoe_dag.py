from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import datetime as dt

import etl.men_shoe_etl as men_etl
import etl.ladies_shoe_etl as ladies_etl
import etl.jnrs_shoe_etl as jnrs_etl

default_args = {
    'owner': 'gavincanete',
    'depends_on_past': False,
    'start_date': dt.datetime(2023, 7, 20),
    'email': ['gavincanete@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

dag = DAG(
      'shoe_dag',
      description='Shoe ETL',
      default_args=default_args,
      schedule=dt.timedelta(seconds=1)
      # schedule='4 * * * *'  -- Crons expression
)

run_men_shoe_etl = PythonOperator(
    task_id='complete_men_shoe_etl',
    python_callable=men_etl.run,
    dag=dag
)

run_ladies_shoe_etl = PythonOperator(
    task_id='complete_ladies_shoe_etl',
    python_callable=ladies_etl.run,
    dag=dag
)

run_jnrs_shoe_etl = PythonOperator(
    task_id='complete_jnrs_shoe_etl',
    python_callable=jnrs_etl.run,
    dag=dag
)

run_men_shoe_etl >> run_ladies_shoe_etl >> run_jnrs_shoe_etl

