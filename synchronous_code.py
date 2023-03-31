import time

TASK_PROCESS_TIME = 5

tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]

for task in tasks:
    print("Starting " + task + "...")
    time.sleep(TASK_PROCESS_TIME)
    print(task + " is done!")



