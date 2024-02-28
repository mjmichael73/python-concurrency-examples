from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def task(task_id):
    print(f"Starting the task {task_id} ...")
    sleep(1)
    return f"Done with task {task_id}"


start_time = perf_counter()

with ThreadPoolExecutor() as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 2)
    print(f1.result())
    print(f2.result())

finish_time = perf_counter()

print(f"It took {finish_time - start_time} second(s) to finish.")
