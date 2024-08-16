from loguru import logger
import requests
import json


def listing_dags():
    url = "http://localhost:8080/api/v1/dags"

    payload = {}
    headers = {
    'Authorization': 'Basic YWlyZmxvdzphaXJmbG93'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # logger.info({response.text})
    response=response.text
    response_dict = json.loads(response)
    # print(response_dict)
    list_of_dag=[]
    for i in response_dict['dags']:
        list_of_dag.append(i['dag_display_name'])

    return list_of_dag
        

    # print(response.text)