dcc.RangeSlider(id='interval', min=-5, max=10, step=1, count=1, value=[-3, 7]),

html.H1('Ending'),
        dcc.Input(
            placeholder='Enter an ending year...',
            type='int',
            value=''
        ),


dash.get_asset_url(image_url)

dcc.Input(id='cycle',
                  placeholder='Enter a cycle length...',
                  type='number',
                  value='11.0'
                  ),


from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import random as rnd
from collections import Counter
from math import floor
import pandas as pd
import sunspotcycle as ssc


df = pd.read_csv('sunspots.csv')
"""
print(df.head())

df['YEAR'] = ''


for i in range(len(df)):
    df['YEAR'][i] = floor(df['MONTH'][i])


print(df.head())
"""


def main():

    # step 1
    app = Dash(__name__)

    # step 2
    app.layout = html.Div([
        html.H3('Starting'),
        dcc.Input(id='starting',
            placeholder='Enter a starting year...',
            type='number',
            value='1749'
        ),
        html.H3('Ending'),
        dcc.Input(id='ending',
            placeholder='Enter an ending year...',
            type='number',
            value='2023'
        ),
        html.H3('Cycle Length'),
        dcc.Slider(id='cycle',
                   min=0,
                   max=22,
                   step=None,
                   value=11
                   ),
        dcc.Graph(id='graph')
    ])

    @app.callback(
        Output('graph', 'figure'),
        Input('starting', 'value'),
        Input('ending', 'value'),
        Input('cycle', 'value')
    )
    def display_value(starting, ending, cycle):
        df = pd.read_csv('sunspots.csv')
        df = df[df['MONTH'] >= float(starting)]
        df = df[df['MONTH'] <= float(ending)]
        df.reset_index(drop=True, inplace=True)
        ssc.df_cycle(df, 'MONTH', float(cycle))


        fig = px.scatter(df, x='MONTH', y='NUM_SUNSPOTS', width=600, height=600)

        fig.update_layout(xaxis_range=[0, cycle],
                          title='Sunspot Cycle: ' + str(cycle),
                          xaxis_title='Years',
                          yaxis_title='# of sunspots')
        return fig
    app.run_server(debug=True)

main()



@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
    def render_content(tab):
        if tab == 'sunspotline':
            return html.Div([
                html.H3('Tab content 1')
            ])
        elif tab == 'sunspotcycle':
            x = tab
        elif tab == 'sunimage':
            return html.Div([
                html.H3('Tab content 3')
            ])


def main():

    # step 1
    app = Dash(__name__)

    # step 2
    app.layout = html.Div([
        html.H1('Starting'),
        dcc.Input(id='starting',
            placeholder='Enter a starting year...',
            type='number',
            value='1749'
        ),
        html.H1('Ending'),
        dcc.Input(id='ending',
            placeholder='Enter an ending year...',
            type='number',
            value='2023'
        ),
        dcc.Graph(id='graph')
    ])

    @app.callback(
        Output('graph', 'figure'),
        Input('starting', 'value'),
        Input('ending', 'value')
    )
    def display_value(starting, ending):
        fig = px.line(df, x='MONTH', y='NUM_SUNSPOTS')

        fig.update_layout(xaxis_range=[starting, ending])
        return fig
    app.run_server(debug=True)


df = pd.read_csv('sunspots.csv')
"""
print(df.head())

df['YEAR'] = ''


for i in range(len(df)):
    df['YEAR'][i] = floor(df['MONTH'][i])


print(df.head())
"""


def main():

    # step 1
    app = Dash(__name__)

    # step 2
    app.layout = html.Div([
        html.H2('Pick a sun imaging filter...'),
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
    ])

    @app.callback(
        Output('img', 'src'),
        Input('radio', 'value')
    )
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
    app.run_server(debug=True)


def cycle_visualization(dfs):
    """ Creates an interactive visualization of sunspot data where the user sets the sunspot cycle

    Args:
        df (pandas.DataFrame): the dataframe that the sunspot data is stored

    Returns:
        html
    """

    # step 1
    app = Dash(__name__)

    # step 2
    app.layout = html.Div([
        html.H3('Starting'),
        dcc.Input(id='starting',
            placeholder='Enter a starting year...',
            type='number',
            value='1749'
        ),
        html.H3('Ending'),
        dcc.Input(id='ending',
            placeholder='Enter an ending year...',
            type='number',
            value='2023'
        ),
        html.H3('Cycle Length'),
        dcc.Slider(id='cycle',
                   min=0,
                   max=22,
                   step=None,
                   value=11
                   ),
        dcc.Graph(id='graph')
    ])

    @app.callback(
        Output('graph', 'figure'),
        Input('starting', 'value'),
        Input('ending', 'value'),
        Input('cycle', 'value')
    )
    def display_value(starting, ending, cycle):
        df = dfs
        df = df[df['MONTH'] >= float(starting)]
        df = df[df['MONTH'] <= float(ending)]
        df.reset_index(drop=True, inplace=True)
        ssc.df_cycle(df, 'MONTH', float(cycle))


        fig = px.scatter(df, x='MONTH', y='NUM_SUNSPOTS', width=600, height=600)

        fig.update_layout(xaxis_range=[0, cycle],
                          title='Sunspot Cycle: ' + str(cycle),
                          xaxis_title='Years',
                          yaxis_title='# of sunspots')
        return fig
    return app.layout