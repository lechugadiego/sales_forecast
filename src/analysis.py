import pandas as pd
import sqlite3
from scipy import stats
import plotly.express as px

def load_and_analyze_data():
    # Connect to database
    conn = sqlite3.connect('database/sales.db')
    
    # Load data
    df = pd.read_sql_query("""
        SELECT 
            date,
            product_name,
            quantity,
            unit_price,
            region,
            quantity * unit_price as revenue
        FROM sales
    """, conn)
    
    # Basic statistical analysis
    summary_stats = df.groupby('product_name')['revenue'].agg([
        'mean',
        'median',
        'std'
    ]).round(2)
    
    # Create simple visualization
    fig = px.bar(
        df.groupby('region')['revenue'].sum().reset_index(),
        x='region',
        y='revenue',
        title='Revenue by Region'
    )
    
    return summary_stats, fig 