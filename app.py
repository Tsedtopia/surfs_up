from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world"
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")
app = Flask(__Welcome__)
//  @app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
flask run
app = Flask(__precipitation__)
@app.route("/api/v1.0/precipitation")  
def precipitation():
    return 
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   return
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   return
{
"city" : {
"name" : "des moines",
        "region" : "midwest"
}
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
app = FLASK(__stations__)
@app.route("/api/v1.0/stations")
def stations():
    return
def stations():
results = session.query(Station.station).all()
    return
def stations():
results = session.query(Station.station).all()
stations = list(np.ravel(results))
return jsonify(stations=stations)
app = Flask(__temp_monthly__)
@app.route("/api/v1.0/tobs")
def temp_monthly():
    return
def temp_monthly():
prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    return
def temp_monthly():
prev_year = dt.date(2017, 8, 23) -dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
filter(Measurement.station == 'USC00519281').\
filter(Measurement.date >= prev_year).all()
    return
def temp_monthly():
prev_year = dt.date(2017, 8, 23) -dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Mesurement.date >= prev_year).all()
    temps = list(np.ravel(results))
        return jsonify(temps=temps)
flask run
app = FLASK(__stats__)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats():
    return
def stats(start=None, end=None):
    return
def stats():
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
                filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    flask run
/api/v1.0/temp/2017-06-01/2017-06-30
["temps":[71.0,77.21989528795811,83.0]]


