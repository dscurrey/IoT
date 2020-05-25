from flaskapp import app, db
from flaskapp.models import SensorData, DangerLevel
from flask import render_template, request, jsonify
import datetime
from flaskapp.dangercalc import danger_calculation

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
    danger_level = danger_calculation(baro_pressure, light, humidity, avg_temp)

    sensordata = SensorData(timestamp=timestamp, baro_pressure=baro_pressure,light=light,humidity=humidity, avg_temp=avg_temp, danger_level=danger_level)
    
    db.session.add(sensordata)
    db.session.commit()

    return jsonify(), 201

@app.route("/graph")
def graph():
    line_labels = ['']

    line_values = SensorData.getAll()
    line_values.sort(key=lambda x: x.timestamp)
    line_values = line_values[-12:]

    return render_template('graph.html', title='Average Temperature Graph', max=40, labels=line_labels, values=line_values)
