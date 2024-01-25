"""
File: sunspotline.py
Description: HTML and a function that runs the app callback for the HTML for a sunspot line graph
Author: Nathan Parker
Date: 16 October 2023
"""
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import random as rnd
from collections import Counter
from math import floor
import pandas as pd

# HTML format that will display the data and provide interaction
sunspotline_html = [
        html.H4('Starting'),
        dcc.Input(id='starting1',
            placeholder='Enter a starting year...',
            type='number',
            value='1749'
        ),
        html.H4('Ending'),
        dcc.Input(id='ending1',
            placeholder='Enter an ending year...',
            type='number',
            value='2023'
        ),
        dcc.Graph(id='graph1')
    ]

# Provides the callback framework used to adjust the sunspotline HTML
def sunspotline_callback(app, dfs):
    """ Callback framework that is used in tandem with the html to create a visualization

    Args:
        app (dash.Dash): the Dash app that contains the layout
        dfs (pd.DataFrame): Dataset that is being pulled from for sunspot data
    """
    @app.callback(
        Output('graph1', 'figure'),
        Input('starting1', 'value'),
        Input('ending1', 'value')
    )
    def display_value(starting1, ending1):
        fig = px.line(dfs, x='MONTH', y='NUM_SUNSPOTS')

        fig.update_layout(xaxis_range=[starting1, ending1],
                          title='International sunspot numbers',
                          xaxis_title='Time (years)',
                          yaxis_title='Sunspot Number')
        return fig