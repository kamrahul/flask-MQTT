import logging
import sys
from xml.etree.ElementInclude import include
from flask_mqtt import Mqtt

# celery for worker
from celery import Celery
from flask import Flask


celery = Celery(__name__, include=["apps.module.task"])
mqtt_client= Mqtt()

def create_app():
    
    # Create flask app object
    app = Flask(__name__)

    # Setting configuration for the project 
    app.config.from_object('config.Config')

    # Adding log level
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.INFO)

    # Celery configuration for service to support celery task
    celery.conf.update(app.config)

    # from gevent import monkey
    # monkey.patch_all()

    # MQTT configuration
    # mqtt_client = Mqtt(app)
    # with app.app_context():
    mqtt_client.init_app(app)

    #mqtt_client = Mqtt(app)


    #Register blueprint
    from apps.module.controller import dummy_module
    app.register_blueprint(dummy_module)

    #Register blueprint mqtt
    from apps.mqtt.controller import mqtt_pubsub
    app.register_blueprint(mqtt_pubsub) 

    return app


def create_celery():
     # Create flask app object
    app = Flask(__name__)

    # Setting configuration for the project 
    app.config.from_object('config.Config')

    # Adding log level
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.INFO)

    # Celery configuration udapte
    celery.conf.update(app.config)

    # from gevent import monkey
    # monkey.patch_all()

    # MQTT configuration
    # mqtt_client = Mqtt(app)
    # with app.app_context():
    mqtt_client.init_app(app)


    #Register blueprint
    from apps.module.controller import dummy_module
    app.register_blueprint(dummy_module)

        #Register blueprint mqtt
    from apps.mqtt.controller import mqtt_pubsub
    app.register_blueprint(mqtt_pubsub) 

    return app



    

