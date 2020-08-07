# import datetime as dt
# import numpy as np
# # import pandas as pdimport
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
from flask import Flask, render_template 
from scrape_mars import scrape
import pymongo
from flask_pymongo import PyMongo

# flask setup
app = Flask(__name__)

# Create connection, DB
# conn = 'mongodb://localhost:27017/mars_db'
# client = pymongo.MongoClient(conn)
# db = client

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# mongo = PyMongo(app, url="mongodb://localhost:27017/mars_db")

# db.mars_tbl.drop()

# db.mars_tbl.insert_one(mars_data)

#############################################
# /api/
#############################################

@app.route("/")
def home():
    my_data = mongo.db.mars_tbl.find_one()
    return render_template("index.html", my_data = my_data)
    # print(mars_data_fromDB)

                                              
if __name__ == '__main__':
    app.run(debug=False)
