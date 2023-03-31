from celery_tasks import intensive_task


def main(jobs_to_run):
    tasks = []

    # Add tasks to the list
    for task in jobs_to_run:
        tasks.append(task)

    print("All your tasks are being worked on.")
    print("You can run some more code here while your workers are working...")

    # Call the tasks asynchronously using Celery
    task_results = [intensive_task.delay(task) for task in tasks]

    # Wait for all tasks to finish and get their results
    for task_result in task_results:
        task_id = task_result.get()
        print(f"Task {task_id} returned successfully.")


if __name__ == "__main__":
    print("Generating some jobs")
    jobs = (f"Task {i}" for i in range(10000))
    main(jobs)
