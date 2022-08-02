#from distutils.log import debug
#from anyio import typed_attribute
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4('Analysis of Iris using scatter Matrix'),
        dcc. Dropdown(
            id= "dropdown",
            options = ['sepal-length', 'sepal_width', 'petal_length', 'petal_width'], # column names
            value= ['sepal_length', 'sepal_width'],
            multi= True
        ),
        dcc.Graph(id = 'graph'),
    ],
)

@app.callback(
    Output('graph', 'figure'), 
    Input('dropdown', 'value'))

def update_bar_chart(dims):
    df = px.data.iris()
    fig = px.scatter_matrix(
        df, dimensions=dims, color = 'species'
    )
    return fig
if __name__ == "__main__":
    app.run_server(debug = True)