from bluepy.btle import BTLEException
from bluepy.sensortag import SensorTag
import time

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

    print("Pressure:\t{}hPa".format(readings["pressure"]))
    print("Baro Temp:\t{}°C".format(readings["baro_temp"]))
    print("Light:\t{}".format(readings["light"]))
    