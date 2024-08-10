# Dynamic_DAG<br>
DAG Template Generator using FastAPI and Python<br>

## Description:<br>

This project is designed to simplify the creation of Directed Acyclic Graphs (DAGs) in Apache Airflow. It uses FastAPI to provide a user-friendly interface where inputs can be submitted via a request body in Swagger UI. The application then generates a DAG script using the BashOperator based on the provided input.

## Features:<br>

**Input via Swagger UI:** Users can input necessary parameters through the FastAPI Swagger UI.<br>
**BashOperator Support:** The generated DAG template utilizes the BashOperator for task execution in Airflow.<br>
**Customizable:** Users can easily modify the template to include additional operators or tasks.<br>


## Installation:<br>

1.**Clone the Repository:**<br>

```git clone https://github.com/yourusername/your-repository-name.git```<br>
```cd your-repository-name```<br>

2.**Create a Virtual Environment:**<br>

```python3 -m venv env```<br>
``` source env/bin/activate  # On Windows use `env\Scripts\activate` ```<br>

3.**Install Dependencies**:<br>

```pip install -r requirements.txt```<br>

4.**Run the FastAPI Application:**<br>

```uvicorn main:app --reload --port 1234```<br>

5.**Access the Swagger UI:**<br>

Open your browser and navigate to http://127.0.0.1:1234/docs. You can input the required parameters for your DAG here.<br>

6.**Generate the DAG Script:**<br>

After submitting your input, the DAG script will be generated and can be saved for use in Apache Airflow.<br>


## Parameters:<br>

1.**dag_name:** The name of the DAG to be created.<br>
2.**conn_id:** The connection ID that Airflow will use to connect to external systems.<br>
3.**schedule_interval:** The schedule interval for the DAG, defining how often it runs (e.g., @daily, 0 12 * * *).<br>
4.**owner:** The owner of the DAG, typically the name of the person or team responsible.<br>
5.**start_date:** The date from which the DAG should start running.<br>
6.**tasks:** A list of tasks to be included in the DAG, with each task containing specific attributes like task_id, bash_command, etc.<br>

## Example:<br>
**STEP 1 :** <br>

Click on POST and then click on Try it out in the Swagger UI.

![1st_dag_example](https://github.com/user-attachments/assets/a76ebb66-d661-4f3d-a69e-1728b0690d64)


**STEP 2 :** <br>

Enter the required parameters for creating a DAG and then click on Execute.

![2nd_dag_example](https://github.com/user-attachments/assets/b5978aab-ab58-4d2f-9839-be2a5688d143)


**STEP 3 :** <br>

After successful execution  response code  200 and "Dag creation request initiated" message will be displayed in response body.

![3rd_dag_example](https://github.com/user-attachments/assets/5580c613-d3be-4ec1-baef-d27366ff010d)


**STEP 4 :** <br>

To run the DAG in Airflow UI search the DAG in All DAGS or Active DAGS and the activate it.

![4th_dag_example](https://github.com/user-attachments/assets/fbb48ec4-1436-4801-bc42-19fd7fb2fe6c)


**STEP 5 :** <br>

Click to RUN the DAG.

![5th_dag_example](https://github.com/user-attachments/assets/60a321ed-1c93-4e00-a764-0a17e529ee91)


**STEP 6 :** <br>

On a successful Run of the DAG UI will be like this. 

![6th_dag_example](https://github.com/user-attachments/assets/5804e5a9-530d-4f67-a48a-61b4777249e1)


## Contributing:<br>

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.<br>

## License:<br>

This project is licensed under the MIT License.<br>
