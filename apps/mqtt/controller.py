import os
from os import curdir
from flask import Blueprint, Flask, current_app, request, jsonify
from apps.factory import mqtt_client 
from flask_mqtt import Mqtt
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
#token = "7aQsi7-L0VpkA32i6xtb1_yHiEFaHjoQM8ib4oR2bJswXGXdGC7vWCQdpOO9zCYbgimwJT8PsyW6_beF8cb1vg=="
#org = "rahul"
#bucket = "temperature"

#client = InfluxDBClient(url="http://localhost:8086", token=token)
# setting up blueprint
mqtt_pubsub= Blueprint('mqtt_pubsub',__name__,url_prefix='/mqtt_pubsub')

#mqtt_client = Mqtt(current_app)
device_name = os.getenv('DEVICE_NAME','123')

@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')  
        print('DEVICE_NAME',device_name)
        mqtt_client.subscribe(device_name) # subscribe topic
        #mqtt_client.subscribe('123') # subscribe topic
    else:
        print('Bad connection. Code:', rc)



@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    try:
        data = dict(
            topic=message.topic,
            payload=message.payload.decode()
        )
        #point = Point("mem").tag("host", "host1").field("used_percent", 23.43234543).time(datetime.utcnow(), WritePrecision.NS)
        #write_api.write(bucket, org, point)
        #data = "mem,host=host1 used_percent=23.43234543"
        #write_api.write(bucket, org, data)
        print('Received message on topic: {topic} with payload: {payload}'.format(**data))
        #current_app.logger.warning('Received message on topic: {topic} with payload: {payload}'.format(**data))
    except Exception as e:
        print(e.message, e.args)


# @mqtt_pubsub.route('/publish', methods=['POST'])
# def publish_message():
#    request_data = request.get_json()
#    publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])
#    return jsonify({'code': publish_result[0]})