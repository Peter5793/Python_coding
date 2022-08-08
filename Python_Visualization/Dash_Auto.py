import pandas as pd 
import dash 
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go 
import plotly.express as px
from dash import no_update

app = dash.Dash(__name__)

# clear the layouts and do not dispaly exception till callbacks gets executed
app.config.suppress_callback_exceptions = True

# read the automobiles data into pandas dataframe
auto_data = pd.read_csv('automobileEDA.csv', 
                        encoding= 'ISO-8859-1',)

# Layout section of dash
app.layout = html.Div( children= [
                    #3A
                    html.H1('Car Automobile Components',
                    style={'textAlign':'center', 'color': '#503D36',
                    'font-size': 24}),
# A outer division starts
    html.Div([
        # first inner divsion for adding dropdown helper text for selected Drive wheels
                html.Div(
                    #3B                   
                        html.H2('Drive Wheels Type:' , style={'margin-right': '2em'}),
                ),
                # 3C
                dcc.Dropdown(
                    id= 'demo-dropdown', 
                    options= [
                        {'label':'Rear Wheel Drive', 'value':'rwd'},
                        {'label':'Front Wheel Drive', 'value':'fwd'},
                        {'label':'Four Wheel Drive', 'value':'4wd'}
                    ],
                    value= 'rwd'
                ),
                # inner division for adding 2 inner divisions for output graphs
                html.Div([
                    
                        html.Div([], id = 'plot1'),
                        html.Div([], id='plot2')
                    
                     ], style= {'display': 'flex'}),
    ])
    # end of outer division
])
# layout ends

# add @app.callback Decorator
@app.callback([Output(component_id = 'plot1', component_property='children'),
            Output(component_id='plot2', component_property='children')],
            Input(component_id='demo-dropdown', component_property = 'value'))
# place to define callback function
# 3F
def display_selected_drive_charts(value):
   filtered_df = auto_data[auto_data['drive-wheels']==value].groupby(['drive-wheels','body-style'],as_index=False). \
            mean()

   filtered_df = filtered_df

   fig1 = px.pie(filtered_df, values='price', names='body-style', title="Pie Chart")
   fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')

   return [dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2) ]
if __name__ == "__main__":
    app.run_server()
    