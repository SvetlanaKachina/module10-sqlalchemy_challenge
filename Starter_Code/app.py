# Import dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

# Database setup
database_path = "sqlite:///hawaii.sqlite"
engine = create_engine(database_path)
Base = automap_base()
Base.prepare(engine, reflect=True)

# Reflect tables
measurement = Base.classes.measurement
station = Base.classes.station

# Initialize Flask app
app = Flask(__name__)

# Define Homepage Route
@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Welcome to the Climate API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Last 12 months of precipitation data<br/>"
        f"/api/v1.0/stations - List of weather stations<br/>"
        f"/api/v1.0/tobs - Temperature observations for the most active station in the last 12 months<br/>"
        f"/api/v1.0/&lt;start&gt; - Min, Avg, and Max temperature from start date<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt; - Min, Avg, and Max temperature for date range<br/>"
    )

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)


import sqlite3
# Connect to the database
conn = sqlite3.connect("hawaii.sqlite")
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in Database:", tables)

conn.close()
