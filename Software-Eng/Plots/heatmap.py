import plotly.offline as pyo
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['record_max_temp_year'].values.tolist(),
                    colorscale = 'Jet')]

# Preparing layout
layout = go.Layout(title='Record Max Temperature', xaxis_title="Day of Week",
                yaxis_title="Month of Year")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherHeatmap.html')