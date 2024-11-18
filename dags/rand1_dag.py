from airflow.decorators import dag, task
from pendulum import datetime
from dags.utils.calculations import * # todo: import it correctly

TASKS = len(batches)
@dag(
    start_date=datetime(2024, 11, 12),
    schedule="0 * * * *",
    max_active_tasks=TASKS,
    catchup=False,
    tags=["Random", "Computations"]
)
def rand1_dag():

    @task(
        queue="medium"
    )
    def medium_computations(batch, factor):
        print(f"Computing batch [{batch}]")
        result = compute_factor(int(factor))
        print(result)

    medium_computations.partial(factor="{{ var.value.medium_factor }}").expand(batch=batches)

rand1_dag()
