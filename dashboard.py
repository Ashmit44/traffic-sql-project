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

# Convert paid to boolean explicitly
data['paid'] = data['paid'].astype(bool)

app.layout = html.Div([
    html.H2("Traffic Fines Dashboard", style={'textAlign': 'center', 'margin': '20px'}),
    
    html.Div([
        dcc.Graph(id='violation-distribution'),
        dcc.Graph(id='payment-status'),
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'gap': '20px'}),
    
    html.Div([
        html.H4("Total Outstanding Fines:", style={'marginBottom': '10px'}),
        html.Div(id='outstanding-amount', 
                style={'color': '#d62728', 'fontSize': '28px', 'padding': '10px',
                       'border': '2px solid #d62728', 'borderRadius': '5px',
                       'display': 'inline-block'})
    ], style={'textAlign': 'center', 'margin': '30px'})
])

@app.callback(
    Output('violation-distribution', 'figure'),
    Input('violation-distribution', 'id'))
def update_violation_pie(_):
    fig = px.pie(data, names='description', title='Violation Type Distribution')
    fig.update_traces(
        textposition='outside',
        textinfo='percent',
        pull=[0.02]*len(data),
        marker=dict(line=dict(color='#ffffff', width=2)),
        rotation=20  # Rotate pie for better label placement
    )
    fig.update_layout(
        uniformtext_minsize=12,
        uniformtext_mode='hide',
        legend=dict(
            orientation="v",  # Changed to vertical
            yanchor="auto",
            xanchor="left",
            x=1.05,  # Move legend to right side
            y=0.5,
            title_text='Violation Types',
            font=dict(size=10)
        ),
        margin=dict(r=150)  # Add right margin for legend
    )
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
                title='Payment Status Overview', 
                text='Count',
                color='Status',
                color_discrete_map={'Paid': '#2ca02c', 'Unpaid': '#d62728'})
    fig.update_layout(
        showlegend=False,
        yaxis_title="Number of Challans",
        xaxis_title="Payment Status"
    )
    fig.update_traces(
        textfont_size=14,
        textangle=0,
        textposition="outside",
        cliponaxis=False
    )
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