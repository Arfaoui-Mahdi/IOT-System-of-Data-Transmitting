from serial import *
import paho.mqtt.client as mqtt

mqttBroker = "broker.hivemq.com"
mqttTopic = "ing_TP_domo_pubsh"

client = mqtt.Client()


def on_connect(client, userdata , flags , rc):
    client.subscribe(mqttTopic)


def on_message(client,userdata, msg):
    temp = float(msg.payload)
    if temp > 30:
      print("la temperature = ",temp," est elevee, ouvrir ventilo")
    else:
      print("la temperature est normale = ",temp)
     #print(str(msg.payload))

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 120)

client.loop_forever()
