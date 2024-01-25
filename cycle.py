"""
File: cycle.py
Description: HTML and a function that runs the app callback for the HTML of a variable sunspot cycle
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
import sunspotcycle as ssc

# HTML format that will display the data and provide interaction
cycle_html = [html.H4('Starting'),
                dcc.Input(id='starting2',
                          placeholder='Enter a starting year...',
                          type='number',
                          value='1749'
                          ),
                html.H4('Ending'),
                dcc.Input(id='ending2',
                          placeholder='Enter an ending year...',
                          type='number',
                          value='2023'
                          ),
                html.H4('Cycle Length'),
                dcc.Slider(id='cycle',
                           min=0,
                           max=22,
                           step=None,
                           value=11
                           ),
                dcc.Graph(id='graph2')]

# Provides the callback framework used to adjust the suncycle HTML
def suncycle_callback(app, df_input):
    """ Callback framework that is used in tandem with the html to create a visualization

    Args:
        app (dash.Dash): the Dash app that contains the layout
        dfs (pd.DataFrame): Dataset that is being pulled from for sunspot data
    """
    @app.callback(
        Output('graph2', 'figure'),
        [Input('starting2', 'value')],
        [Input('ending2', 'value')],
        [Input('cycle', 'value')]
    )
    def display_value(starting2, ending2, cycle):
        df = df_input
        df = df[df['MONTH'] >= float(starting2)]
        df = df[df['MONTH'] <= float(ending2)]
        df.reset_index(drop=True, inplace=True)
        ssc.df_cycle(df, 'MONTH', float(cycle))

        fig = px.scatter(df, x='MONTH', y='NUM_SUNSPOTS', width=600, height=600)

        fig.update_layout(xaxis_range=[0, cycle],
                          title='Sunspot Cycle: ' + str(cycle),
                          xaxis_title='Years',
                          yaxis_title='# of sunspots')
        return fig