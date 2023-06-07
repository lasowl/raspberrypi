import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import psutil
import adafruit_dht
import json


for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein':
        proc.kill()

dht_device = adafruit_dht.DHT22(4)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 23

GPIO.setup(LED,GPIO.OUT)

MQTT_HOST = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_SUB_TOPIC = "mobile/20221036/led"              
MQTT_PUB_TOPIC = "mobile/20221036/sensing"


def on_publish(client, userdata, mid):
    print("\nMessage published...")
      
def on_message(client, userdata, message):
    result = str(message.payload.decode("utf-8"))
    print("received message = ", str(message.payload.decode("utf-8")))
    if result.upper() == "ON":
        print("LED ON !!!")
        GPIO.output(LED, GPIO.HIGH)
    elif result.upper() == "OFF":
        print("LED OFF !!!")
        GPIO.output(LED, GPIO.LOW)
    else:
        print("Illegal Argument Exception!")

client = mqtt.Client()
client.on_message = on_message
client.on_publish = on_publish
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.subscribe(MQTT_SUB_TOPIC)
client.loop_start()

try:
    while True :
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            sensing = {
                "temperature" : temperature,
                "humidity" : humidity,
                }
            
            current_time=time.strftime("%H:%M:%S")
            print(current_time,end="",flush=True)
            time.sleep(1)
            print("\r")
            
            value = json.dumps(sensing)
            client.publish(MQTT_PUB_TOPIC,value)
            
            
            print(value)
            
            if temperature >= 26:
                GPIO.output(LED,GPIO.HIGH)
                print("overheated")

        except RuntimeError as error:
            time.sleep(0)
            continue

        time.sleep(5)
        
        
except KeyboardInterrupt:
    print("종료합니다!!")
finally:
    client.disconnect()
