import pandas as  pd
import plotly.express as px
import dash
import dash_html_components as html 
import dash_core_components as dcc  

# read the airline data into the dataframe
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
                            'IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                            encoding = "ISO-8859-1",
                            dtype = {'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# sample 500 data points setting random stae to be 42 so that we get same result
data = airline_data.sample(n=500, random_state = 42)
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')   

# create dash application
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                        style= {'textAlign': 'center', 'color': '#503d36',
                                        'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by' 
                                'flights', style = {'textAlign':'center', 'color':'#f5741'}),
                                dcc.Graph(figure=fig)
                                ])
# Run the application
if __name__ == "__main__":
    app.run_server()