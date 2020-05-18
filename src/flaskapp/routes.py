from flaskapp import app, db
from flaskapp.models import SensorData
from flask import render_template, request, jsonify
import datetime

@app.route("/")
@app.route("/index")
def index():
    data = SensorData.query.order_by(SensorData.timestamp.desc())
    return render_template('index.html', title='Home', data=data)

@app.route('/', methods=["POST"])
def newdata():
    baro_temp = request.json['baro_temp']
    baro_pressure = request.json['baro_pressure']
    light = request.json['light']
    humidity_temp = request.json['humidity_temp']
    humidity = request.json['humidity']
    timestamp = datetime.datetime.now()

    sensordata = SensorData(timestamp=timestamp,baro_temp=baro_temp, baro_pressure=baro_pressure,light=light,humidity_temp=humidity_temp,humidity=humidity)
    
    db.session.add(sensordata)
    db.session.commit()

    return jsonify(), 201

