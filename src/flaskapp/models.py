from flaskapp import db

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer)

    def __repr__(self):
        return '<SensorData {}>'.format(self.temperature)