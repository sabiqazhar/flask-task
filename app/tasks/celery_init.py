from celery import Celery
from celery.schedules import crontab
from app.service.MailService import MailService

# redis_broker_url = 'redis://guest:@localhost:6379/'
broker_url = 'amqp://guest:guest@localhost:5672/'
app = Celery('tasks', backend='rpc://', broker=broker_url)
app.conf.beat_schedule = {
    'send-mail': {
        'task': 'app.tasks.CeleryInit.sendToday',
        'schedule': crontab()
    },
}

"""
im using default crontab (task run every minute)
"""

@app.task
def sendToday():
    MailService.send()