from celery import shared_task
import time

@shared_task
def addition(a,b):
    time.sleep(10)
    return a+b

@shared_task
def send_msg():
    print('sample msg send to email')