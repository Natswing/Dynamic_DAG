from schema.schema import *
from loguru import logger
from template.template_1 import template_1,template_2
from datetime import datetime



def dag_file_logic(user_request_body):
    logger.info(f"{user_request_body}")
    # logger.info(f"{template1}")
    dag_name=user_request_body['dag_name']
    conn_id=user_request_body['conn_id']
    schedule_interval=user_request_body['schedule_interval']
    owner=user_request_body['owner']
    logger.info(f"{user_request_body['start_date']}")
    start_date=datetime.strptime(user_request_body['start_date'],"%d/%m/%Y")
    start_date=start_date.date()
    logger.info(f"{start_date}")
    template1=template_1(owner,dag_name,start_date,schedule_interval)
    final_script=template1
    task_dependency=''
    task_list=user_request_body['tasks']
    for task in task_list:
        for key ,value in task.items():
            template2=template_2(key,value)
            final_script+=template2
            task_dependency+=key+">>"
    # logger.info(f"{key},{value}")
    task_dependency=task_dependency[:-2]
    logger.info({task_dependency})
    final_script+=task_dependency

    with open('dag.py', 'w') as file:
        file.write(f"{final_script}")
        # file.write(f"{template2}")