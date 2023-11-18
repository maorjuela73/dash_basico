# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div([
    html.H1(children='Gráfico de frutas en diferentes lugares'),

    html.Div(children='''
        Dash: Ejemplo de gráfico de barras usado en los talleres Knuth, 2023-2.
    '''),

    html.Img(src="https://placehold.co/600x400"),

    dcc.Checklist(
      df.City.unique(),
      value=[],
      id='check-escogido'
    ),

    dcc.Graph(
        id='barritas' )
    ])

@callback(
  Output('barritas', 'figure'),
  Input('check-escogido', 'value')
)
def actualizar_grafico(value):
  df_filtrado = df[df.City.isin(value)]
  return px.bar(df_filtrado, x="Fruit", y="Amount", color="City", barmode="group")


if __name__ == '__main__':
    app.run(debug=True)
