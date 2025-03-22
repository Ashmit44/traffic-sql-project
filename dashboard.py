import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from db import engine

app = dash.Dash(__name__)

# Load and merge data
challans = pd.read_sql("SELECT * FROM challans", engine)
violations = pd.read_sql("SELECT * FROM violations", engine)
data = pd.merge(challans, violations, on='violation_code')

app.layout = html.Div([
    html.H2("Traffic Fines Dashboard", style={'textAlign': 'center', 'margin': '20px'}),
    
    html.Div([
        dcc.Graph(id='violation-distribution'),
        dcc.Graph(id='payment-status'),
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),
    
    html.Div([
        html.H4("Total Outstanding Fines:"),
        html.Div(id='outstanding-amount', 
                style={'color': 'red', 'fontSize': '28px', 'padding': '10px'})
    ], style={'textAlign': 'center', 'margin': '30px'})
])

@app.callback(
    Output('violation-distribution', 'figure'),
    Input('violation-distribution', 'id')
)
def update_violation_pie(_):
    fig = px.pie(data, names='description', title='Violation Type Distribution')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

@app.callback(
    Output('payment-status', 'figure'),
    Input('payment-status', 'id')
)
def update_payment_chart(_):
    status_counts = data['paid'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    status_counts['Status'] = status_counts['Status'].map({True: 'Paid', False: 'Unpaid'})
    
    fig = px.bar(status_counts, x='Status', y='Count', 
                title='Payment Status Overview', text='Count',
                color='Status', color_discrete_map={'Paid': '#2ca02c', 'Unpaid': '#d62728'})
    fig.update_layout(showlegend=False)
    return fig

@app.callback(
    Output('outstanding-amount', 'children'),
    Input('outstanding-amount', 'id')
)
def update_outstanding_total(_):
    total = data.loc[data['paid'] == False, 'fine_amount'].sum()
    return f"₹{total:,.2f}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)