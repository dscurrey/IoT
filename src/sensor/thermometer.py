from bluepy.btle import BTLEException
from bluepy.sensortag import SensorTag
import time
import requests

SENSOR_ADDRESS = '54:6C:0E:53:12:D5'

tag = SensorTag(SENSOR_ADDRESS)
tag.connect(tag.deviceAddr, tag.addrType)

def enable_sensors(tag):
    tag.barometer.enable()
    tag.lightmeter.enable()
    time.sleep(1)

def disable_sensors(tag):
    tag.barometer.disable()
    tag.lightmeter.disable()

def get_readings(tag):
    try:
        enable_sensors(tag)
        readings = {}
        readings["baro_temp"],readings["pressure"]=tag.barometer.read()
        readings["light"]=tag.lightmeter.read()
        disable_sensors(tag)    
        return readings
    except BTLEException as e:
        print(e)
        return {}
    
while(True):
    print('------------------------------------')
    readings = get_readings(tag)

    # Testing POST
    r = requests.post("localhost:5000", data={'temp':readings["baro_temp"]})
    print(r.status_code)
