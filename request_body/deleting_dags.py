from fastapi import FastAPI,HTTPException
from schema.schema import *
from loguru import logger
import requests
   

def delete_dags(del_dag_body):
    dag_name=del_dag_body["dag_name"]
    url = f"http://localhost:8080/api/v1/dags/{dag_name}"

    headers = {
    'Authorization': 'Basic YWlyZmxvdzphaXJmbG93'
    }

    response = requests.delete(url, headers=headers)
    # logger.info({response.text})
    if response.status_code==404:
        raise HTTPException(status_code=404,detail=f"DAG '{dag_name}' not found")
    if response.status_code!=204:
        raise HTTPException(status_code=response.status_code,detail=f"Failed to delete dag.")
    # response=response.text
    # response_dict = json.loads(response)
    # for i in response_dict['dags']:
    #     if i["dag_display_name"]==dag_name:
    #         response_dict["dags"].pop(i)
    # return True
    return {"message":"Deleted successfully."}



    

