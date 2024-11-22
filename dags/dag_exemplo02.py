# modelo mais moderno, que usa decoradores

import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

@dag(dag_id="primeira_dag_com_decorator",
    description="minha etl",
    start_date=datetime.datetime(2024, 11, 22),
    schedule="@daily", 
    catchup=False #backfill - reprocessa tudo que estava anteriormente
)

def gerar_dag():
    EmptyOperator(task_id="tarefa")

gerar_dag()