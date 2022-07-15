from distutils.debug import DEBUG
import os
from datetime import timedelta
from celery.schedules import crontab

class Config(object):
    DEBUG = True

    # Worker configuration
    BROKER_URL ="redis://redis:6379/0"
    CELERY_RESULT_BACKEND ="redis://redis:6379/0"
    CELERY_DEFAULT_QUEUE ="test_queue"
    CELERYBEAT_SCHEDULE = {
    'periodic_task': {
        'task': 'apps.module.task.periodic_task',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}


    # MQTT Brocker Configuration 
    MQTT_BROKER_URL = 'broker.emqx.io'
    MQTT_BROKER_PORT=1883
    MQTT_USERNAME=""
    MQTT_PASSWORD=""
    MQTT_KEEPALIVE=5
    MQTT_TLS_ENABLED=False


    #Device Configuration
    DEVICE_NAME = os.getenv('DEVICE_NAME','123')

