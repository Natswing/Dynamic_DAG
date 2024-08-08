
from datetime import timedelta
import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
'owner': 'vaishnavi',
'retries':2,
'retry_delay':timedelta(minutes=2),

}

with DAG(
dag_id = 'testing_dag',
default_args = default_args,
start_date = datetime.datetime.strptime('2024-08-03', "%Y-%m-%d"),
schedule_interval = None
) as dag:

    
    task1 = BashOperator(
    task_id = 'task1',
    bash_command = 'echo vaishnavi1'
    )
    
    task2 = BashOperator(
    task_id = 'task2',
    bash_command = 'echo vaishnavi2'
    )
    
    task3 = BashOperator(
    task_id = 'task3',
    bash_command = 'echo vaishnavi3'
    )
    task1>>task2>>task3