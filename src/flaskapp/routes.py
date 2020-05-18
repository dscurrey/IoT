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
    baro_temp = round(request.json['baro_temp'], 2)
    baro_pressure = round(request.json['baro_pressure'], 2)
    light = round(request.json['light'], 2)
    humidity_temp = round(request.json['humidity_temp'], 2)
    humidity = round(request.json['humidity'], 2)
    avg_temp = round((baro_temp + humidity_temp)/2, 2)
    timestamp = datetime.datetime.now()

    sensordata = SensorData(timestamp=timestamp, baro_pressure=baro_pressure,light=light,humidity=humidity, avg_temp=avg_temp)
    
    db.session.add(sensordata)
    db.session.commit()

    return jsonify(), 201

