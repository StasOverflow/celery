from celery import Celery
from celery.schedules import crontab


app = Celery(__name__, broker='redis://localhost', backend='redis://localhost')
app.conf.update({'beat_schedule': {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*'),  # minute='2, 35' << only 2nd and 35th minute of an hour
        'args': (16, 16)
        },
    }
})   # accepts a dict with configurations


@app.task
def add(x, y):
    return x + y

# activate worker with: celery -A tasks worker --loglevel=info
# activate task with: add.delay(1, 4)
#                 or: add.apply_async(args=[4,9], countdown=10)
#                 or: add.apply_async(args=[4,9], eta=datetime.datetime.now())
