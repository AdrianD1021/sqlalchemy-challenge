import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#Last 12 Months

last_12_months = '2016-08-23'


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Welcome to the Hawaii Station API"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/Precipitation<br/>"
        f"/api/v1.0/Stations<br/>"
        f"/api/v1.0/Tobs<br/>"
        f"/api/v1.0/Start<br/>"
        f"/api/v1.0/Start_End<br/>"
    )


@app.route("/api/v1.0/Precipitation")
def precipitation_12():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Measurements"""
    # Query for Precipitation
    precipitation_results = session.query(Measurement.prcp).filter(Measurement.date >= last_12_months).group_by(Measurement.date).all()

    session.close()

    return jsonify(precipitation_results)


@app.route("/api/v1.0/Stations")
def stationnames():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query for Stations
    station_names = session.query(Station.name).all()

    session.close()

    return jsonify(station_names)

@app.route("/api/v1.0/Tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query for Tobs
    tobs = session.query(Measurement.tobs).all()

    session.close()

    return jsonify(tobs)

@app.route("/api/v1.0/Start")
def start(date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query for Start Date
    start_date = session.query(function.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >=date).all()

    session.close()

    return jsonify(start_date)

@app.route("/api/v1.0/Start_End")
def startend(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query for Start and End Date
    start_end_query = session.query(function.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >=start).filter(Measurement.date<=end).all()

    session.close()

    return jsonify(start_end_query)

if __name__ == '__main__':
    app.run(debug=True)