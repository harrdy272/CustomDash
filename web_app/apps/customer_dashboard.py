import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_daq as daq

from web_app.app import app
from web_app.apps.helpers.helper_functions import get_extended_values, get_random_city, get_random_gender, get_random_age, get_random_segment

import pandas as pd
import numpy as np
from random import random

COLORS = {
    'background': '#28283c',
    'text': '#77d1d6',
}

customer_id = 1
MONTHS = ['August', 'September', 'October', 'November', 'December', 'January']


def generate_arpu_graph(customer):
    return {
        'data': [
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[customer]['ARPU']),
                'type': 'bar',
                'marker': {
                    'color': '#63b7af',
                    'size': 10,
                },
                'width': [0.4] * 6,
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
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 1000]
            },
        }
    }


def generate_service_usage_graph(customer):
    return {
        'data': [
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[customer]['Internet Usage']),
                'name': 'Internet Usage',
                'marker': {
                    'color': '#ff9d76',
                    'size': 10,
                }
            },
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[customer]['Voice Usage']),
                'name': 'Voice Usage',
                'marker': {
                    'color': '#a3f7bf',
                    'size': 10,
                }
            },
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[customer]['SMS Usage']),
                'name': 'SMS Usage',
                'marker': {
                    'color': '#05dfd7',
                    'size': 10,
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
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 1000]
            },
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
                html.Strong('Customer ID :  ', className='info-title'),
                html.Strong('1', id='display-customer-id', className='info-value'),
            ], className='text-customer-id'),
            html.P([
                html.Strong('Location :  ', className='info-title'),
                html.Strong('Mumbai', className='info-value', id='location'),
            ], className='text-customer-id'),
            html.P([
                html.Strong('Age :  ', className='info-title'),
                html.Strong('40-45', className='info-value', id='age'),
            ], className='text-customer-id'),
            html.P([
                html.Strong('Gender :  ', className='info-title'),
                html.Strong('M', className='info-value', id='gender'),
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
    ], id='last-div'),
    # dcc.Link('Go to App 2', href='/apps/overall_dashboard')
])


@app.callback(
    [Output('display-customer-id', 'children'),
     Output('location', 'children'),
     Output('age', 'children'),
     Output('gender', 'children')],
    [Input('submit-button', 'n_clicks')],
    [State('customer-id', 'value')],
)
def update_customer_id(n_clicks, value):
    return value, get_random_city(), get_random_age(), get_random_gender()


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
