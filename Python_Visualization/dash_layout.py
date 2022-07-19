# import the required packages
import pandas as pd 
import dash 
import dash_core_components as dcc  
import dash_html_components as html 
import plotly.express as px 
from dash.dependencies import Input, Output

#TODO add dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount" :[4,1,2,2,4,5],
    "City": ["SF","SF","SF","NYC","MTL","NYC"]
})
#TODO add a bargraph figure
fig = px.bar(df, x = 'Fruit', y = 'Amount', color = 'City', barmode= 'group')
app = dash.Dash()
app.layout = html.Div(children= [
    html.H1(
            children= 'Portfolio Dashboard',
            style= {
                'textAlign':'center'
            }
        ),
        # create dropdown
        dcc.Dropdown( options= [
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
            ],
        value= 'NYC' # default value in the dropdown
        ),
        # Bar graph
        dcc.Graph(id='example-graph-2', figure=fig)
    ])
# run application
if __name__ == "__main__":
    app.run_server()