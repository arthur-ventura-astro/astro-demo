from airflow.decorators import dag, task
from pendulum import datetime
from plugins.utils import * # todo: import it correctly

TASKS = len(batches)
@dag(
    start_date=datetime(2024, 11, 12),
    schedule="*/5 * * * *",
    max_active_tasks=TASKS,
    catchup=False,
    tags=["Random", "Computations"]
)
def rand5_dag():

    @task
    def easy_computations(batch):
        print(f"Computing batch [{batch}]")
        result = compute_factor(factor=1)
        print(result)

    easy_computations.expand(batch=bathces)

rand5_dag()
