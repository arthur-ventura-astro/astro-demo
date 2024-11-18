from airflow.decorators import dag, task
from pendulum import datetime
from dags.utils.calculations import * # todo: import it correctly

TASKS = len(batches)
@dag(
    start_date=datetime(2024, 11, 12),
    schedule="0 0 * * *",
    max_active_tasks=TASKS,
    catchup=False,
    tags=["Random", "Computations"]
)
def rand2_dag():

    @task(
        queue="hard"
    )
    def hard_computations(batch, factor):
        print(f"Computing batch [{batch}]")
        result = compute_factor(factor=int(factor))
        print(result)

    hard_computations.partial(factor="{{ var.value.hard_factor }}").expand(batch=batches)

rand2_dag()
