from flask import Flask
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html

# commonly used css stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# spinup flask server
server = Flask(__name__)

# spinup dash app on flask server
app = Dash(__name__, server=server, external_stylesheets=external_stylesheets)

# app html layout
app.layout = html.Div([
    
    # classic hello world statement for proof of success
    html.Div([
        html.H1("Hello from Dash!"),
    ], style={'textAlign': "center"}),

])

if __name__ == '__main__':
    # run server
    app.run_server(debug=True)
