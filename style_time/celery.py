import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'style_time.settings')

app = Celery('style_time')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
