from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def task(task_id):
    print(f"Starting the task {task_id} ...")
    sleep(1)
    return f"Done with task {task_id}"


start_time = perf_counter()

with ThreadPoolExecutor() as executor:
    results = executor.map(task, [1, 2])
    for result in results:
        print(result)

finish_time = perf_counter()
print(f"It took {finish_time - start_time} second(s) to finish.")
