# modelo exemplo ultrapassado, funciona.

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

# criando uma instancia do objeto da classe DAG e executo a instancia pelo operador.
minha_dag= DAG(
    dag_id="dag_exemplo1",
    start_date=datetime.datetime(2024,3,23),
    schedule="@daily",
    catchup=False,
)

EmptyOperator(task_id="tarefa",dag=minha_dag)