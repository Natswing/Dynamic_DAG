def template_1(owner,dag_name,start_date,schedule_interval):
 
    template1 = f"""
from datetime import timedelta
import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {{
'owner': '{owner}',
'retries':2,
'retry_delay':timedelta(minutes=2),

}}

with DAG(
dag_id = '{dag_name}',
default_args = default_args,
start_date = datetime.datetime.strptime('{start_date}', "%Y-%m-%d"),
schedule_interval = {schedule_interval}
) as dag:

    """
    return template1

def template_2(task_id,bash_command):
    template2 = f"""
    {task_id} = BashOperator(
    task_id = '{task_id}',
    bash_command = '{bash_command}'
    )
    """
    return template2