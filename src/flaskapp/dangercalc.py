from flaskapp.models import DangerLevel

Critical_Temperature = 105
Critical_Light = 40
Critical_Humididty = 80

def danger_calculation(baro_pressure,light,humidity,avg_temp):
    if avg_temp >= Critical_Temperature:
        return DangerLevel.Critical
    if light >= Critical_Light:
        return DangerLevel.Critical
    if humidity >= Critical_Humididty:
        return DangerLevel.Critical