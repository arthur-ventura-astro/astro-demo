from airflow.decorators import dag, task
from pendulum import datetime
from dags.utils.calculations import * # todo: import it correctly

TASKS = len(batches)
@dag(
    start_date=datetime(2024, 11, 12),
    schedule="*/30 * * * *",
    max_active_tasks=TASKS,
    catchup=False,
    tags=["Random", "Computations"]
)
def rand3_dag():

    @task(
        queue="easy"
    )
    def easy_computations(batch, factor):
        print(f"Computing batch [{batch}]")
        result = compute_factor(int(factor))
        print(result)

    easy_computations.partial(factor="{{ var.value.easy_factor }}").expand(batch=batches)

rand3_dag()
