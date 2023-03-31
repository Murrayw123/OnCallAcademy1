from celery import Celery

# Configure Celery to use RabbitMQ as the message broker
app = Celery("tasks", broker="pyamqp://guest@rabbitmq//")


@app.task
def intensive_task(task_id):
    import time

    print(f"Task {task_id} started.")
    time.sleep(5)
    print(f"Task {task_id} completed.")
    return task_id
