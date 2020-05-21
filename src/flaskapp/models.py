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
