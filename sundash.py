"""
File: sundash.py
Description: Final hw2 file that glues the three dashboard functionalities together
Author: Nathan Parker
Date: 16 October 2023
"""
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import random as rnd
from collections import Counter
from math import floor
import pandas as pd
import sunspotcycle as ssc
import cycle as cyc
import sunspotline as ssl
import sunimage as si

def main():

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    # Read data from the csv
    df = pd.read_csv('sunspots.csv')

    # Step 1: Defining the app object
    app = Dash(__name__, external_stylesheets=external_stylesheets)

    # Step 2: Setup app layout with tabs that lead to different visualizations
    app.layout = html.Div([
        html.H1('Sundash Dashboard'),
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Sunspot Line Data', value='sunspotline', children=ssl.sunspotline_html),
            dcc.Tab(label='Sunspot Cycle Scatter', value='sunspotcycle', children=cyc.cycle_html),
            dcc.Tab(label='Current Sun Image', value='sunimage', children=si.sunimage_html)
        ]),
        html.Div(id='tabs-content')
    ])

    # Step 3: Callback for the different tabs
    si.sunimage_callback(app)

    cyc.suncycle_callback(app, df)

    ssl.sunspotline_callback(app, df)

    # Step 4: Run the server
    app.run_server(debug=True)

main()