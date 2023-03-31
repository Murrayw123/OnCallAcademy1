import time
import threading

TASK_PROCESS_TIME = 1

tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]


def process_task(task):
    print("Starting " + task + "...")
    time.sleep(TASK_PROCESS_TIME)
    print(task + " is done!")


threads = []
for task in tasks:
    thread = threading.Thread(target=process_task, args=(task,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
