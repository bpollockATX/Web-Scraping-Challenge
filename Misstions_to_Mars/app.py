# import datetime as dt
# import numpy as np
# # import pandas as pdimport
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from scrape_mars import scrape

# # db Setup
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# measurement = base.classes.measurement
# station = base.classes.station

# flask setup
app = Flask(__name__)


#############################################
# /api/v1.0/precipitation
#############################################

@app.route("/scrape")
def call_scrape():
    return scrape


                                              
if __name__ == '__main__':
    app.run(debug=False)
