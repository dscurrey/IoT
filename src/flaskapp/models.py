from flaskapp import db

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ir_temp = db.Column(db.Float)
    humidity = db.Column(db.Float)
    baro_temp = db.Column(db.Float)
    baro_pressure = db.Column(db.Float)
    light = db.Column(db.Float)

    def __repr__(self):
        return '<SensorData {}>'.format(self.temperature)