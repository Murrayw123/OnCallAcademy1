import time
import queue
import threading

TASKS = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]


def intensive_task(task_id, results):
    print(f"Task {task_id} started.")
    time.sleep(5)
    print(f"Task {task_id} completed.")
    results.append(task_id)


def main():
    task_queue = queue.Queue()

    # Add tasks to the queue
    for task in TASKS:
        task_queue.put(task)

    results = []
    threads = []

    # Spawn workers for each task
    while not task_queue.empty():
        task_id = task_queue.get()
        task_thread = threading.Thread(target=intensive_task, args=(task_id, results))
        task_thread.start()
        threads.append(task_thread)

    print("All your tasks are being worked on.")
    print("You can run some more code here while your threads are working...")

    for thread in threads:
        thread.join()

    print("All your tasks are done!")


if __name__ == "__main__":
    main()
