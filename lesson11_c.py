from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True)


# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="stock-dropdown",
        options=[{"label": symbol, "value": symbol} for symbol in df.columns],
        value="GOOG"
    ),
    dcc.Graph(id="stock-price")
])

# Callback for dynamic updates
@app.callback(
    Output("stock-price", "figure"),
    [Input("stock-dropdown", "value")]
)
def update_graph(symbol):
    fig = px.line(df, x="date", y=symbol, title=f"{symbol} Price")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 
    
'''
import pandas as pd
from dash import dash_table, Dash, html

app = Dash(__name__)

df = pd.read_csv("some csv file")

app.layout = html.Div([dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], id='tbl')])'''