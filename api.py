from fastapi import FastAPI
from schema.schema import *
from loguru import logger
from request_body.request_body_logic import *

app = FastAPI()

@app.post("/create_dag")
async def root(user_request_body:DagRequestBody):
 user_request_body=user_request_body.model_dump()
 logger.info(f'{user_request_body}')
 result=dag_file_logic(user_request_body)

 return {"message":"Dag creation request initiated."}