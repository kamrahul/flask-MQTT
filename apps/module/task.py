import os
from apps.factory import celery,mqtt_client
from flask import current_app
from datetime import timedelta
import requests
import random





@celery.task(name="worker_name",bind=True,queue="test_que")
def task(self,**kwargs):

    request_params = kwargs.get('test')

    #setting up logs
    current_app.logger.info("Task Received and executed")
    self.update_state(state='PROGRESS',meta={'any_key':'any_value'})
    current_app.logger.info(request_params)


@celery.task()
def periodic_task():
    print('Hi! from periodic_task')
    list1 = ['1', '2', '3', '4', '5','6']
    device_name = os.getenv('DEVICE_NAME','123')
    #publish_result = mqtt_client.publish('server', 'SENSOR DATA '+ device_name)
    data_to_send = {
                        "topic":"server",
                        "msg": "SENSOR "+device_name + ' VALUE - '+random.choice(list1)
                    }
    res = requests.post('http://192.168.1.6:8005/dummy_module/publish', json=data_to_send)
    #print ('response from server:',res.text)

    current_app.logger.info("Data pushed to server")
    current_app.logger.info(data_to_send.get('msg'))
    current_app.logger.info('---------------------------------')