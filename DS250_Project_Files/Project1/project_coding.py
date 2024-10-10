"""
This file is here if you want to do your coding for the project in a Python file
before you copy it to the QMD file
"""
from skimpy import clean_columns
import pandas as pd
import numpy as np
from lets_plot import *
LetsPlot.setup_html()

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from lets_plot import *
LetsPlot.setup_html()

# Sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [10, 15, 13, 17, 9]}

# Create the plot using ggplot
plot = ggplot(data) + geom_line(aes(x='x', y='y'))

# Save the plot as an HTML file
plot.save_as_html(filename="ds250_project_1.html")

print("HTML file has been generated: ds250_project_1.html")


print('This code is running')