Part 1: Analyze and Explore the Climate Data
Used Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database. Used SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, completed the following steps:
1.	Noted the provided files (climate_starter.ipynb and hawaii.sqlite) to complete climate analysis and data exploration.
2.	Used the SQLAlchemy create_engine() function to connect to SQLite database.
3.	Used the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.
4.	Linked Python to the database by creating a SQLAlchemy session.
5.	Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
Precipitation Analysis
1.	Found the most recent date in the dataset.
2.	Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.
3.	Selected only the "date" and "prcp" values.
4.	Loaded the query results into a Pandas DataFrame. Explicitly set the column names.
5.	Sorted the DataFrame values by "date".
6.	Plotted the results by using the DataFrame plot method
7.	Used Pandas to print the summary statistics for the precipitation data.
Station Analysis
1.	Designed a query to calculate the total number of stations in the dataset.
2.	Designed a query to find the most-active stations (that is, the stations that have the most rows). To do so, completed the following steps:
•	Listed the stations and observation counts in descending order.
•	Answered the following question: which station id has the greatest number of observations?
3.	Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4.	Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, completed the following steps:
•	Filtered by the station that has the greatest number of observations.
•	Queried the previous 12 months of TOBS data for that station.
•	Plotted the results as a histogram with bins=12
5.	Closed session.

Part 2: Design Your Climate App
To design a Flask API based on the queries that just developed. To do so, used Flask to create routes as follows:
1.	/
o	Started at the homepage.
o	Listed all the available routes.
2.	/api/v1.0/precipitation
o	Converted the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
o	Returned the JSON representation of your dictionary.
3.	/api/v1.0/stations
o	Returned a JSON list of stations from the dataset.
4.	/api/v1.0/tobs
o	Queried the dates and temperature observations of the most-active station for the previous year of data.
o	Returned a JSON list of temperature observations for the previous year.
5.	/api/v1.0/<start> and /api/v1.0/<start>/<end>
o	Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
o	For a specified start, calculated TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
o	For a specified start date and end date, calculated TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
