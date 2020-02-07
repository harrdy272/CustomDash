import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

sys.path.append(r"D:\Events\VIL Codefest\CustomDash")

from web_app.app import app
from web_app.apps import customer_dashboard, overall_dashboard

app.layout = html.Div([
    dcc.Location(id='url', refresh=False, pathname='/apps/customer_dashboard'),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/apps/customer_dashboard':
        return customer_dashboard.layout
    elif pathname == '/apps/overall_dashboard':
        return overall_dashboard.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
