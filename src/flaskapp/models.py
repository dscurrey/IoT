from flaskapp import db

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Float)
    avg_temp = db.Column(db.Float)
    baro_pressure = db.Column(db.Float)
    light = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    danger_level = db.Column(db.Integer)

    def __repr__(self):
        return '<SensorData {}>'.format(self.id)
    
    @staticmethod
    def getAll():
        return SensorData.query.all()

class DangerLevel():
    Critical = 1 #The server is in a dangerous state, it should be automatically shutdown to prevent damage to components and data loss.
    High = 2 #The server is outside of standard operating conditions, and its state should be manually reviewed to prevent data loss.
    Medium = 3 #The server getting close to the limit of standard operating conditions and should be kept an eye on, but could also be due to sustained load.
    Low = 4 #The server is a little above standard temperatures, however is standard for burst computing.
    Nil = 5 #There is no danger level; data is normal.
    Unknown = 6 #Some data may be incorrect, and the sensor should be checked.
    Tampered = 7 #The server may have been tampered with, such as getting moved or physically accessed.
    Other = 8