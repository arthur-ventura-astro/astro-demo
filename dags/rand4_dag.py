from airflow.decorators import dag, task
from pendulum import datetime
from plugins.utils import * # todo: import it correctly

TASKS = len(batches)
@dag(
    start_date=datetime(2024, 11, 12),
    schedule="*/30 * * * *",
    max_active_tasks=TASKS,
    catchup=False,
    tags=["Random", "Computations"]
)
def rand4_dag():

    @task
    def hard_computations(batch):
        print(f"Computing batch [{batch}]")
        result = compute_factor(factor=50)
        print(result)

    hard_computations.expand(batch=batches)

rand4_dag()
