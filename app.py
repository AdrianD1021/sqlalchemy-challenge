
## Import the dependencies.
import os import datetime as dt
from turtle import end_fill import numpy as np import pandas as pd

import sqlalchemy from sqlalchemy.ext.automap import automap_base from sqlalchemy.orm import Session from 
sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request, url_for, redirect from flask_sqlalchemy import 
SQLAlchemy

from sqlalchemy.sql import func

#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

engine= create_engine("sqlite://hawaii.sqlite")

# reflect the tables

Base = automap_base()

Base.prepare(engine, reflect=True)


# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB

session = Session(engine)


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

@app.route("/")

def first():
    return(
        ***
        Climate Analysis API!
        Available Choices:
        /api/version1/precipitation
        /api/version1/stations
        /api/version1/tobs
        /api/version1/temp/start/end
        ***
    )


#################################################
# Flask Routes
#################################################


