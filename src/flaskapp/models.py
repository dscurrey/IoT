from flaskapp import db

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Float)
    humidity_temp = db.Column(db.Float)
    baro_temp = db.Column(db.Float)
    baro_pressure = db.Column(db.Float)
    light = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<SensorData {}>'.format(self.temperature)