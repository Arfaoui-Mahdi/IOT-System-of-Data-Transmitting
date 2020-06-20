from serial import *
import paho.mqtt.publish as publish

mqttBroker = "broker.hivemq.com"
mqttTopic = "ing_TP_domo_pubsh"

with Serial(port="COM2", baudrate=9600, timeout=1, write_timeout=1) as SP:
    if SP.isOpen():
        while True:
            message = SP.readline()
            message = message.decode("utf-8")
            #message = float(message)
            if message != "":
              print("la temperature est ", message)
              publish.single(mqttTopic, message, hostname=mqttBroker)
