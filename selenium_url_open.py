#import knihoven
import time
import paho.mqtt.client as paho
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Nastavení proměnných
driver = webdriver.Firefox()
driver.get("https://www.hardwario.com/projects/")



broker="127.0.0.1" # adresa MQTT brokeru
client = paho.Client("open-url") # Název clienta

#Callback, který se zavolá při příjmutí zprávy na topicu, na který je subscribe
def on_message(client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        driver.get(msg)

        
def connect():
        global client #globální proměnná
        client.on_message=on_message # Nastavení callbacku

        client.connect(broker) # Připojení k MQTT brokeru

        client.loop_start() # Asynchroní čekání na subscribe zprávy
        client.subscribe("node/selenium/-/url/set")
        while True:
                time.sleep(0.2)
#volání funkce
connect()