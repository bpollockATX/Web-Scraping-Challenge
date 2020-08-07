# import datetime as dt
# import numpy as np
# # import pandas as pdimport
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
from flask import Flask, render_template 
from scrape_mars import scrape
import pymongo

# flask setup
app = Flask(__name__)

# Create connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Create DB, collection
db = client.mars_db



@app.route("/scrape")
def call_scrape():
    my_data = scrape()
    db.mars_tbl.update({}, my_data, upsert = True)
    print(my_data)
                                              
if __name__ == '__main__':
    app.run(debug=False)
