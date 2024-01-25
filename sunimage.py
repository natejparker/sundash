"""
File: sunimage.py
Description: HTML and a function that runs the app callback for the HTML that displays an image
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

# HTML format that will display the data and provide interaction
sunimage_html = [
        html.H4('Pick a sun imaging filter...'),
        dcc.RadioItems(id='radio',
            options=[
                {'label': 'EIT 171', 'value': 0},
                {'label': 'EIT 195', 'value': 1},
                {'label': 'EIT 284', 'value': 2},
                {'label': 'EIT 304', 'value': 3},
                {'label': 'HMI Continuum', 'value': 4},
                {'label': 'HMI Magnetogram', 'value': 5},
                {'label': 'Lasco C2', 'value': 6},
                {'label': 'Lasco C3', 'value': 7}
            ],
            value=4
        ),
        html.Img(id='img', style={'height': '30%', 'width': '30%'})
    ]

# Provides the callback framework used to display images from online
def sunimage_callback(app):
    """ Callback framework that pulls sun images from online and displays them

    Args:
        app (dash.Dash): the Dash app that contains the layout
    """
    @app.callback(
        Output('img', 'src'),
        Input('radio', 'value')
    )
    # Extra Credit Attempt: Supports multiple real time sun image filters
    def display_value(radio):
        x = ''
        match radio:
            case 0:
                x = 'eit_171'
            case 1:
                x = 'eit_195'
            case 2:
                x = 'eit_284'
            case 3:
                x = 'eit_304'
            case 4:
                x = 'hmi_igr'
            case 5:
                x = 'hmi_mag'
            case 6:
                x = 'c2'
            case 7:
                x = 'c3'
        return 'https://soho.nascom.nasa.gov/data/realtime/' + x + '/1024/latest.jpg'