# Flask MQTT

# Steps to follow

## Add flask_mqtt in requirement.txt
## Add Brocker configuration in config.py
## Add Device_name in configuration from environment variable. ( MQTT topic)
## Add Mqtt initialization in app context factory.py
### mqtt_client = Mqtt(app)
## Create Blueprint in app folder 'mqtt'

<br/>

## Add file controller.py
###
balena push g_rahul_k/home --debug
