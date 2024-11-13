from airflow.decorators import dag, task
from pendulum import datetime
from plugins.utils import * # todo: import it correctly

TASKS = len(bathces)
@dag(
    start_date=datetime(2024, 11, 12),
    schedule="*/15 * * * *",
    max_active_tasks=TASKS,
    catchup=False,
    tags=["Random", "Computations"]
)
def random_dag():

    @task
    def hard_computations(batch):
        print(f"Computing batch [{batch}]")
        result = compute_factor()
        print(result)

    hard_computations.expand(batch=bathces)

random_dag()
