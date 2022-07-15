import json
import logging
import queue
from flask import Blueprint,jsonify,current_app,request
from apps.factory import celery,mqtt_client




# setting up blueprint
dummy_module= Blueprint('dummy_module',__name__,url_prefix='/dummy_module')


@dummy_module.route('/test_get',methods=['GET'])
def test_get():
    return jsonify({'test':'tes'})



@dummy_module.route('/test_post',methods=['POST'])
def test_post(**kwargs):


    #setting up logs
    current_app.logger.info(request.json)

    #send response as json
    return jsonify(request.json)


@dummy_module.route('/push_task',methods=['GET'])
def push_task(**kwargs):


    #setting up logs
    current_app.logger.info(request.json)

    #setting up task
    result = celery.send_task('worker_name',kwargs={"test":123},queue="test_que")

    #send response as json
    return jsonify({'task_id': result.task_id})


@dummy_module.route('/publish', methods=['POST'])
def publish_message():
   request_data = request.get_json()

   current_app.logger.info("SEND DATA REQUEST RECEIVED")

   publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])
   return jsonify({'code': publish_result[0]})
