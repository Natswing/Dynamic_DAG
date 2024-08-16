from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional,List,Dict

class DagRequestBody(BaseModel):
    dag_name:str = Field(example="testing_dag")
    conn_id: str= Field(example="local_host")
    schedule_interval:str= Field(example='None')
    owner:str= Field(example="vaishnavi")
    start_date:str= Field(example="3/8/2024")
    tasks:List[Dict[str,str]]= Field(example=[
    {
    "task1": "echo vaishnavi1",
    "task2": "echo vaishnavi2",
    "task3": "echo vaishnavi3"
    }
    ])

class DeleteDag(BaseModel):
    dag_name: str = Field(example="example_dag")