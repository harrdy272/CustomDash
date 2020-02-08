import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_daq as daq

from web_app.app import app

import pandas as pd
import numpy as np
from random import random

COLORS = {
    'background': '#28283c',
    'text': '#77d1d6',
}

customer_id = 1


def get_three_values():
    a = np.random.randint(100, 500)
    b = np.random.randint(100, 500)
    c = np.random.randint(100, 500)
    return [a, b, c]


def get_extended_values(value):
    a = np.random.randint(100, 500)
    b = np.random.randint(100, 500)
    return [a, b, value]


def get_random_segment():
    segments = ['Travel', 'Food', 'Banking', 'War', 'Lifestyle', 'Hacking']
    return segments[np.random.randint(0, 5)]


def generate_arpu_graph(customer):
    return {
        'data': [
            {
                'x': ['June', 'July', 'August'],
                'y': get_extended_values(df.iloc[customer]['ARPU']),
                'type': 'bar'
            },
        ],
        'layout': {
            'title': 'Average Revenue per User',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
        }
    }


def generate_service_usage_graph(customer):
    return {
        'data': [
            {
                'x': ['June', 'July', 'August'],
                'y': get_extended_values(df.iloc[customer]['Internet Usage']),
                'name': 'Internet Usage',
                'marker': {
                    'color': 'rgb(55, 83, 109)'
                }
            },
            {
                'x': ['June', 'July', 'August'],
                'y': get_extended_values(df.iloc[customer]['Voice Usage']),
                'name': 'Voice Usage',
                'marker': {
                    'color': 'rgb(26, 118, 255)'
                }
            },
            {
                'x': ['June', 'July', 'August'],
                'y': get_extended_values(df.iloc[customer]['SMS Usage']),
                'name': 'SMS Usage',
                'marker': {
                    'color': 'rgb(26, 200, 55)'
                }
            }
        ],
        'layout': {
            'title': 'Service Usage by the User',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            }
        }
    }


def generate_churn_probability(prob):
    random_prob = np.random.randint(0, 100)
    return html.Div(
        id='churn-probability',
        children=str(random_prob) + "%"
    )


df = pd.read_csv(r"D:\Events\VIL Codefest\CustomDash\web_app\appdata\sample_plotting.csv")

layout = html.Div([
    html.Div([
        html.Div([
            html.H3(
                html.Strong(
                    '''
                    CUSTOMDASH
                    ''', id='customdash'),
            ),
            html.Div([
                dcc.Input(
                    id='customer-id',
                    type='number',
                    placeholder='Enter Customer ID...',
                    value=1,
                    className='eight columns'
                ),
                html.Button('Submit', id='submit-button', className='four columns'),
            ], className='container', style={'width': '100%'})
        ], className='six columns'),

        html.Div([
            html.P([
                html.Strong('Customer ID: '),
                html.Strong('1', id='display-customer-id'),
            ], className='text-customer-id'),
        ], className='six columns container', id='customer-info')
    ], className='container'),

    html.Div([
        html.Div([
            dcc.Graph(
                id='arpu-graph',
                style={'width': '100%'},
                figure=generate_arpu_graph(customer_id))
        ], className='six columns', style={'width': '48%'}),

        html.Div([
            dcc.Graph(
                id='service-usage-graph',
                figure=generate_service_usage_graph(customer_id)),
        ], className='six columns'),

    ], className='container'),

    html.Div([
        html.Div([
            html.Div([
                html.Strong('CHURN PROBABILITY', className='titles'),
                generate_churn_probability(1)
            ], className='six columns', id='display-customer-churn'),
            html.Div([
                html.Strong('CUSTOMER SEGMENT', className='titles'),
                html.Div([
                    get_random_segment()
                ], id='customer-segment')
            ], className='six columns', id='display-customer-segment')
        ], className='container'),

        # dcc.Link('Go to App 2', href='/apps/overall_dashboard')
    ], id='last-div')
])


@app.callback(
    Output('display-customer-id', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')],
)
def update_customer_id(n_clicks, value):
    return value


@app.callback(
    Output('service-usage-graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def service_usage_graph(n_clicks, value):
    return generate_service_usage_graph(value)


@app.callback(
    Output('arpu-graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def update_arpu_graph(n_clicks, value):
    return generate_arpu_graph(value)


@app.callback(
    Output('churn-probability', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def update_churn_probability(n_clicks, value):
    return str(np.random.randint(0, 100)) + "%"


@app.callback(
    Output('customer-segment', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')]
)
def update_customer_segment(n_clicks, value):
    return get_random_segment()
