from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args =  {
    'owner' : 'mhmd1001',
    'depends_on_past' : False,
    'start_date' : datetime(2023, 12, 7)
}


dag = DAG (
        'ow3a_wishak', 
        default_args = default_args, 
        description = 'simple dag', 
        schedule_interval = '@daily',
)

def first_task():
    print('Hello World')

def second_task():
    print('Hey, This is the second task')


task1 = PythonOperator(
    task_id ='task1',
    python_callable = first_task,
    dag = dag
)


task2 = PythonOperator(
    task_id = 'task2',
    python_callable = second_task,
    dag = dag
)



task1 >> task2
