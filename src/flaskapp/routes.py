from flaskapp import app, db
from flaskapp.models import SensorData
from flask import render_template, request, jsonify

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route('/', methods=["POST"])
def newdata():
    temp = request.json['temp']
    sensordata = SensorData(temperature=temp)
    
    db.session.add(sensordata)
    db.session.commit()

    return jsonify(), 201

