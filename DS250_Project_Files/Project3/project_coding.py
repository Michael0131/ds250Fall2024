"""
This file is here if you want to do your coding for the project in a Python file
before you copy it to the QMD file
"""

import pandas as pd
import numpy as np
from lets_plot import *
LetsPlot.setup_html()
import sqlite3

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


con = sqlite3.connect('DS250_Project_Files\\Project3\\lahmansbaseballdb.sqlite')
# Write the SQL query

query = "SELECT CAST(H AS FLOAT) / AB AS batting_average FROM batting WHERE playerID = 'addybo01' AND yearID = '1871'"
df = pd.read_sql_query(query, con)

print(df.round(3))
# we use player ID: addybo01
# then we need to get the AB in batting


# Load any data you need for the report
# df = pd.read_csv('filename.csv')

