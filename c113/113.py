import pandas as pd
import statistics
import plotly.express as px
import numpy as np
#Uploading the csv
from google.colab import files
data_to_load = files.upload()

#Plotting the graph
df = pd.read_csv("2data.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()