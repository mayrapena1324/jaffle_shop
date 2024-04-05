import datetime

from airflow.decorators import dag
from operators.datacoves.dbt import DatacovesDbtOperator

@dag(
    default_args={
        'start_date': datetime.datetime(2023, 1, 1, 0, 0),
        'owner': 'Mayra Pena',
        'email': 'mayraapena2016@gmail.com',
        'email_on_failure': True,
    },
    description='A DAG to run dbt for the Jaffle Shop project',
    schedule_interval='0 7 * * *',
    tags=['version_3'],
    catchup=False,
)
def yaml_dbt_dag():
    run_dbt = DatacovesDbtOperator(
        task_id='run_dbt',
        bash_command='dbt build'
    )

dag = yaml_dbt_dag()
