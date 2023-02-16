from datetime import datetime, timedelta
from textwrap import dedent


from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

with DAG(
    "example_dag",
    description="this is a sample dag",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],

) as dag:

    task1=BashOperator(
        task_id="task1",
        bash_command="sleep 5",
    )

    task2=BashOperator(
        task_id="task2",
        bash_command="sleep 5",
    )

    task3=BashOperator(
        task_id="task3",
        bash_command="exit 125",
        retries= 5,
        retry_delay= timedelta(seconds=2)
    )

    task4=BashOperator(
        task_id="task4",
        bash_command="sleep 2",
    )


    task1 >> [task2,task3] >> task4