# This project is from Udacity Data Engnerring nano Degree 

# Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. 
This project is to help them to design a DBS with star schema to help ther analytic team to optimize queries on song play analysis. It also build ETL pipeline to assitant them to extract,transform the data from json files and load to the dbsystem.

# How to Work
To run this code, please ensure you have already installed python3.

There are three python files called sql_queries.py,elt.py,create_tables.py

sql_queries.py stores all the queries, elt.py is the elt pipeline files,and create_tables.py is the file to create DB and tables.

if you want to run these code, be sure that you have to run create_tables.py first, and then run etl.py

data file includes all the data that need to be process in the etl pipelines.