from datetime import datetime

from airflow.decorators import dag, task
from airflow.models.baseoperator import chain

from time import sleep

@dag(start_date=datetime(2024, 3, 23), 
     schedule="@daily", 
     catchup=False)
def segunda_dag_com_python_operator():
    """
    minha primeira Pipipeline
    """
    @task
    def primeira_atividade():
        return "Atividade Sequencial finalizada"

    @task
    def segunda_atividade(response):
        print(response)
        sleep(1)
        print("Segunda atividade finalizada")

    @task
    def terceira_atividade():
        print("Terceira atividade iniciada")
        sleep(1)
        print("Terceira atividade finalizada")
    
    @task
    def quarta_atividade():
        print("Pipeline finalizado.")

    t1 = primeira_atividade()
    t2 = segunda_atividade(t1)
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    # t1 >> t2 >> t3 >> t4 # sequencia um apos o outro
    chain(t1,t2,t3,t4)

    # t1 >> [t2,t3]  # sequencia t1, depois t2 e y3 ao mesmo tempo 
    # t3 << t4 # t4 roda antes de t3
    # first_task.set_downstream([second_task, third_task]) # igual a de cima, no entanto usando explicitamente o metodo
    # third_task.set_upstream(fourth_task)

segunda_dag_com_python_operator()