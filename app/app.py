import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(name, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
  html.H1(children='Hello Dash'),
])

if name == 'main':
  app.run_server(host='0.0.0.0', port=8080, debug=True)