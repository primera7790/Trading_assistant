import os
from celery import Celery
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_assistant.settings')

app = Celery('trading_assistant')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'init_auto_mode': {
#         'task': 'main_interface.tasks.auto_mode_task',
#         'schedule': crontab(minute='*/2'),
#     },
# }
