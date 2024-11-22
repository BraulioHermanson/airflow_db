# modelo exemplo ultrapassado, funciona.

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

# iniciando um contexto para criar dag
with DAG(
    dag_id="dag_exemplo1",
    start_date=datetime.datetime(2021,1,1),
    schedule="@daily",
    catchup=False
):
    EmptyOperator(task_id="tarefa")