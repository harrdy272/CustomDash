import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_daq as daq

from web_app.app import app

import pandas as pd
import numpy as np
from random import random


def get_three_values():
    a = np.random.randint(100, 500)
    b = np.random.randint(100, 500)
    c = np.random.randint(100, 500)
    return [a, b, c]


def get_extended_values(value):
    a = np.random.randint(100, 500)
    b = np.random.randint(100, 500)
    c = np.random.randint(100, 500)
    return [a, b, value]


def get_random_segment():
    segments = ['Travel', 'Food', 'Banking', 'War', 'Lifestyle', 'Hacking']
    return segments[np.random.randint(0, 5)]


customer_id = np.random.randint(0, 99)

df = pd.read_csv(r"D:\Events\VIL Codefest\CustomDash\web_app\appdata\sample_plotting.csv")

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                dcc.Markdown('''
                    **Customer ID: **
                '''),
                html.Div(id='display-customer-id'),
            ], className='col'),
            html.Div([
                html.H3(
                    dcc.Markdown('''
                        **CUSTOMDASH**
                    '''),
                ),
                dcc.Input(id='customer-id', type='number', placeholder='Enter Customer ID...', value=1),
                html.Button('Submit', id='submit-button'),
            ], 'col')
        ], className='row'),
    ], className='container-fluid'),

    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    id='arpu-graph',
                    figure={
                        'data': [
                            {'x': ['June', 'July', 'August'], 'y': get_three_values(), 'type': 'bar'},
                        ],
                        'layout': {
                            'title': 'Average Revenue per User'
                        }
                    },
                ),

            ], className='col'),
            html.Div([
                dcc.Graph(
                    figure=dict(
                        data=[
                            dict(
                                x=['June', 'July', 'August'],
                                y=get_extended_values(df.iloc[customer_id]['Internet Usage']),
                                name='Internet Usage',
                                marker=dict(
                                    color='rgb(55, 83, 109)'
                                )
                            ),
                            dict(
                                x=['June', 'July', 'August'],
                                y=get_extended_values(df.iloc[customer_id]['Voice Usage']),
                                name='Voice Usage',
                                marker=dict(
                                    color='rgb(26, 118, 255)'
                                )
                            ),
                            dict(
                                x=['June', 'July', 'August'],
                                y=get_extended_values(df.iloc[customer_id]['SMS Usage']),
                                name='SMS Usage',
                                marker=dict(
                                    color='rgb(26, 200, 55)'
                                )
                            )
                        ],
                        layout=dict(
                            title='Service Usage by the User',
                            showlegend=True,
                            legend=dict(
                                x=0,
                                y=1.0
                            ),
                            # margin=dict(l=40, r=10, t=40, b=30)
                        )
                    ), id='service-usage-graph'
                )
            ], className='col'),
        ], className='row no-gutters')
    ], className='container-fluid'),

    html.Div([
        html.Div([
            html.Div([
                dcc.Markdown('''**Churn Probability: **'''),
                html.Div([
                    random(),
                ], id='churn-probability'),
            ], className='col'),
            html.Div([
                dcc.Markdown('''
                    **Customer Segment: **
                    '''),
                html.Div([
                    get_random_segment()
                ], id='customer-segment')
            ], className='col')
        ], className='row')
    ], className='container-fluid'),

    # dcc.Link('Go to App 2', href='/apps/overall_dashboard')
])


@app.callback(
    Output('display-customer-id', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def update_customer_id(n_clicks, value):
    return value


@app.callback(
    Output('service-usage-graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def service_usage_graph(n_clicks, value):
    return dict(
        data=[
            dict(
                x=['June', 'July', 'August'],
                y=get_extended_values(df.iloc[value]['Internet Usage']),
                name='Internet Usage',
                marker=dict(
                    color='rgb(55, 83, 109)'
                )
            ),
            dict(
                x=['June', 'July', 'August'],
                y=get_extended_values(df.iloc[value]['Voice Usage']),
                name='Voice Usage',
                marker=dict(
                    color='rgb(26, 118, 255)'
                )
            ),
            dict(
                x=['June', 'July', 'August'],
                y=get_extended_values(df.iloc[value]['SMS Usage']),
                name='SMS Usage',
                marker=dict(
                    color='rgb(26, 200, 55)'
                )
            )
        ],
        layout=dict(
            title='Service Usage by the User',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            transition={'duration': 500}
            # margin=dict(l=40, r=10, t=40, b=30)
        )
    )


@app.callback(
    Output('arpu-graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def update_arpu_graph(n_clicks, value):
    return {
        'data': [
            {'x': ['June', 'July', 'August'], 'y': get_three_values(), 'type': 'bar'},
        ],
        'layout': {
            'title': 'Average Revenue per User'
        }
    }


@app.callback(
    Output('churn-probability', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def update_arpu_graph(n_clicks, value):
    return random()


@app.callback(
    Output('customer-segment', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def update_arpu_graph(n_clicks, value):
    return get_random_segment()

