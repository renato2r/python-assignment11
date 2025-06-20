import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load built-in gapminder dataset
df = pldata.gapminder()

# Get unique country names
countries = df['country'].unique()

# Create the Dash app
app = dash.Dash(__name__)

server = app.server #<-- For cloud deploy, if needed -->

# Define layout
app.layout = html.Div([
    html.H1("🌍 GDP Per Capita Growth by Country"),

    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada',  # Initial value
        placeholder="Select a country"
    ),

    dcc.Graph(id='gdp-growth')
])

# Define callback to update graph based on selected country
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f'📈 GDP Per Capita Growth in {selected_country}',
        labels={'gdpPercap': 'GDP per Capita', 'year': 'Year'}
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
