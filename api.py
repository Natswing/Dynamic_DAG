from fastapi import FastAPI
from schema.schema import *
from loguru import logger
from request_body.request_body_logic import *
from request_body.listing_dags import *
from request_body.deleting_dags import *


app = FastAPI()

@app.post("/create_dag")
async def root(user_request_body:DagRequestBody):
 user_request_body=user_request_body.model_dump()
 logger.info(f'{user_request_body}')
 result=dag_file_logic(user_request_body)

 return {"message":"Dag creation request initiated."}

@app.get("/list_of_dags")
async def list_dags():
    result=listing_dags()
    return result

@app.delete("/delete_dags")
async def delete_dag(del_dag_body:DeleteDag):
   del_dag_body=del_dag_body.model_dump()
   result=delete_dags(del_dag_body)
   return result
   

   

    
