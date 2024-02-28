from time import sleep, perf_counter
from threading import Thread


def task(task_id):
    print(f"Starting the task {task_id}")
    sleep(1)
    print(f"The task {task_id} is done")

start_time = perf_counter()

threads = []

for i in range(1, 11):
    t = Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

end_time = perf_counter()

print(f"It took {end_time - start_time: 0.2f} second(s) to complete.")