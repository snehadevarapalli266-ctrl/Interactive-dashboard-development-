# Interactive Dashboard Development
# Author: Sneha Devarapally

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# 1. Create sample business dataset
data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Sales": [
        12000, 15000, 14000, 18000, 22000, 20000,
        25000, 28000, 26000, 30000, 32000, 35000
    ],
    "Profit": [
        2000, 3000, 2500, 4000, 5000, 4500,
        6000, 7000, 6500, 8000, 8500, 9500
    ],
    "Marketing": [
        1000, 1200, 1100, 1500, 1800, 1700,
        2000, 2200, 2100, 2500, 2600, 2800
    ]
}

df = pd.DataFrame(data)

# 2. Calculate key performance indicators
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_sales = df["Sales"].mean()

print("BUSINESS PERFORMANCE SUMMARY")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Monthly Sales:", round(average_sales, 2))

# 3. Create charts
sales_chart = px.line(
    df,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

profit_chart = px.bar(
    df,
    x="Month",
    y="Profit",
    title="Monthly Profit"
)

marketing_chart = px.bar(
    df,
    x="Month",
    y="Marketing",
    title="Monthly Marketing Expenses"
)

# 4. Build interactive dashboard
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Business Performance Dashboard"),

    html.Div([
        html.Div([
            html.H3("Total Sales"),
            html.H2(f"${total_sales:,.0f}")
        ]),

        html.Div([
            html.H3("Total Profit"),
            html.H2(f"${total_profit:,.0f}")
        ]),

        html.Div([
            html.H3("Average Monthly Sales"),
            html.H2(f"${average_sales:,.0f}")
        ])
    ], style={
        "display": "flex",
        "justifyContent": "space-around",
        "textAlign": "center"
    }),

    dcc.Graph(figure=sales_chart),
    dcc.Graph(figure=profit_chart),
    dcc.Graph(figure=marketing_chart),

    html.H3("Business Insights"),
    html.Ul([
        html.Li("Monitor monthly sales trends."),
        html.Li("Compare profits across different months."),
        html.Li("Evaluate marketing expenses against sales."),
        html.Li("Use performance metrics to support decisions.")
    ])
])

# 5. Run the dashboard
if __name__ == "__main__":
    app.run(debug=False)
