from flaskapp import app, db
from flaskapp.models import SensorData
from flask import render_template, request, jsonify

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route('/', methods=["POST"])
def newdata():
    baro_temp = request.json['baro_temp']
    baro_pressure = request.json['baro_pressure']
    light = request.json['light']
    humidity_temp = request.json['humidity_temp']
    humidity = request.json['humidity']

    sensordata = SensorData(baro_temp=baro_temp, baro_pressure=baro_pressure)
    
    db.session.add(sensordata)
    db.session.commit()

    return jsonify(), 201

