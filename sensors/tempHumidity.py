#!/home/chestnut/venv-piFarm/bin/python3

import Adafruit_DHT as dht

def readDHT():
    humidity, temperature = dht.read_retry(11,4)
    temperature = temperature * 9/5.0 + 32
    #print (temperature)
    #print (humidity)
    return temperature
