from bluepy.btle import BTLEException
from bluepy.sensortag import SensorTag
import time

SENSOR_ADDRESS = '54:6C:0E:53:12:D5'

tag = SensorTag(SENSOR_ADDRESS)
tag.connect(tag.deviceAddr, tag.addrType)

def enable_sensors(tag):
    tag.IRtemperature.enable()
    tag.accelerometer.enable()
    tag.humidity.enable()
    tag.magnetometer.enable()
    tag.barometer.enable()
    tag.gyroscope.enable()
    tag.keypress.enable()
    tag.lightmeter.enable()
    time.sleep(1)

def disable_sensors(tag):
    tag.IRtemperature.disable()
    tag.accelerometer.disable()
    tag.humidity.disable()
    tag.magnetometer.disable()
    tag.barometer.disable()
    tag.gyroscope.disable()
    tag.keypress.disable()
    tag.lightmeter.disable()

def get_readings(tag):
    try:
        enable_sensors(tag)
        readings = {}
        readings["gyro"] = tag.gyroscope.read()
        readings["accele"] = tag.accelerometer.read()
        readings["ir_temp"],readings["ir"] = tag.IRtemperature.read()
        readings["humidity_temp"],readings["humidity"] = tag.humidity.read()
        readings["baro_temp"],readings["pressure"] = tag.barometer.read()
        readings["light"] = tag.lightmeter.read()
        disable_sensors(tag)
        
        return readings
    except BTLEException as e:
        print("Beans.")
        print(e)
        return {}
    
while(True):
    print('------------------------------------')
    readings = get_readings(tag)
    print("Gyro:\t{}".format(readings["gyro"]))
    print("Accelerometer:\t{}".format(readings["accele"]))
    print("IR Temp:\t{}".format(readings["ir_temp"]))
    print("IR:\t{}".format(readings["ir"]))
    print("Humidity Temp:\t{}".format(readings["humidity_temp"]))
    print("Humidity:\t{}".format(readings["humidity"]))
    print("Baro Temp:\t{}".format(readings["baro_temp"]))
    print("Barometer Pressure:\t{}".format(readings["pressure"]))
    print("Light:\t{}".format(readings["light"]))