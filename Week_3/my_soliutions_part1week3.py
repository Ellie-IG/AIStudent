# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:44:31 2025

@author: ellen

# Part 1
## Story:
At Netflix competitor, BingeBlitz, a sudden influx of new subscribers has caused a massive increase in demand, leading to noticeable latency and occasional buffering issues during peak streaming hours. The backend engineer, Alex, is tasked with optimizing the service to handle the load more efficiently. To make informed decisions, Alex seeks insights from you.

You have access to a data warehouse with 50+ M rows of data called `BingeBlitz.db`. Note, you need to create `BingeBlitz.db` by running `uv run synthetic_data.py`. Note,this requires `uv` to be installed. This may take a couple of minutes. `BingeBlitz.db` has the following tables:

1. `streaming_data` - Contains information about the streaming sessions, including `title_id`, `bandwidth`, `time_measured`, `region`, `resolution`, and `device`.

2. `title_data` - Contains details about the titles, including `title_id`, `title_name`, `genre`, and `release_year`.

3. `viewership_data` - Contains data about the viewership of titles, including `title_id`, `viewership`, and `time_day`.

## Task 1: Aggregations
Which titles are consuming the most bandwidth?
(Objective: Identify high-demand content and evaluate if caching or CDNs can prioritize these titles.)

What are the peak usage times across different regions?
(Objective: Plan for regional load balancing and optimize server resource allocation.)

What are the most common resolutions and devices being used? Answer as a proportion of total usage.
(Objective: Determine if adaptive bitrate streaming can be fine-tuned for specific device profiles or resolutions.)
"""
import numpy as np
import pandas as pd
import sqlite3
'''
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@localhost:3306/BingeBlitz")
with engine.connect() as conn, conn.begin():
    data = pd.read_sql_table("streaming_data", conn)
    #binge = pd.read_sql_table('streaming_data', conn)'''

conn = sqlite3.connect("BingeBlitz.db")

# Create a cursor object to execute queries
cursor = conn.cursor()

# Verify connection by listing tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:", tables)

# Close the connection when done
conn.close()

"""
## Task 2: Joins
Are there specific genres or types of content that spike during particular hours or days?
(Objective: Prepare for predictable demand patterns by preloading data or increasing server capacity temporarily.)
"""



"""
## Task 3: Window Functions
Which titles have the fastest growth in viewership per day in the last week?
(Objective: To identify content that is rapidly gaining popularity and allow server capacity to be scaled up.)


"""

