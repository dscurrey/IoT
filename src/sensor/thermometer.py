from bluepy.btle import BTLEException
from bluepy.sensortag import SensorTag
import time
import requests

SENSOR_ADDRESS = '54:6C:0E:53:12:D5'
API = "http://192.168.0.21:5000"

INTERVAL = 10

tag = SensorTag(SENSOR_ADDRESS)
tag.connect(tag.deviceAddr, tag.addrType)

print("Connected to sensor")

def enable_sensors(tag):
    
    tag.barometer.enable()
    tag.IRtemperature.enable()
    tag.humidity.enable()
    tag.lightmeter.enable()
    time.sleep(1)

def disable_sensors(tag):
    tag.barometer.disable()
    tag.IRtemperature.disable()
    tag.humidity.disable()
    tag.lightmeter.disable()

def get_readings(tag):
    try:
        enable_sensors(tag)
        readings = {}
        readings["baro_temp"],readings["pressure"]=tag.barometer.read()
        readings["light"]=tag.lightmeter.read()
        readings["humidity_temp"],readings["humidity"] = tag.humidity.read()
        disable_sensors(tag)    
        return readings
    except BTLEException as e:
        print(e)
        return {}
    
while(True):
    time.sleep(INTERVAL)
    readings = get_readings(tag)

    # POST
    data = {
        'baro_temp':readings["baro_temp"],
        'baro_pressure':readings["pressure"],
        'light':readings["light"],
        'humidity_temp':readings['humidity_temp'],
        'humidity':readings['humidity']
    }

    r = requests.post(url=API, json=data)

    print(r.status_code)
