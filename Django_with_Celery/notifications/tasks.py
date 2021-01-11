from celery import shared_task
import time

@shared_task
def addition(a,b):
    time.sleep(10)
    return a+b