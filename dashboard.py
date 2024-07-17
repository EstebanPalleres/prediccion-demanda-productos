import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import requests

app_dash = dash.Dash(__name__)

app_dash.layout = html.Div([
    html.H1("Predicciones de Demanda de Productos"),
    html.Div([
        dcc.Input(id='input-year', type='number', placeholder='Año', min=2000, max=2100, step=1),
        dcc.Input(id='input-month', type='number', placeholder='Mes', min=1, max=12, step=1),
        dcc.Input(id='input-day', type='number', placeholder='Día', min=1, max=31, step=1),
        dcc.Input(id='input-season', type='number', placeholder='Estación', min=1, max=4, step=1),
        dcc.Input(id='input-promotion', type='number', placeholder='Promoción', min=0, max=1, step=1),
        dcc.Input(id='input-event', type='number', placeholder='Evento', min=0, max=1, step=1),
    ]),
    html.Button('Predecir', id='predict-button'),
    html.Div(id='output-prediction')
])

@app_dash.callback(
    Output('output-prediction', 'children'),
    [Input('predict-button', 'n_clicks')],
    [State('input-year', 'value'), State('input-month', 'value'), State('input-day', 'value'),
     State('input-season', 'value'), State('input-promotion', 'value'), State('input-event', 'value')]
)
def update_output(n_clicks, year, month, day, season, promotion, event):
    if n_clicks is None or year is None or month is None or day is None or season is None or promotion is None or event is None:
        return 'Por favor, ingrese todos los valores.'
    
    features = [year, month, day, season, promotion, event]
    try:
        response = requests.post('http://127.0.0.1:5000/predict', json={'features': features})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        prediction = response.json()['prediction']
        return f'Predicción de Demanda: {prediction}'
    except requests.exceptions.RequestException as e:
        print(f"Error al llamar a la API: {e}")
        return f"Error al predecir: {e}"

if __name__ == '__main__':
    app_dash.run_server(debug=True)
