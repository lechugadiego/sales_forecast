import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create connection
conn = sqlite3.connect('database/sales.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    date DATE,
    product_name TEXT,
    quantity INT,
    unit_price DECIMAL(10,2),
    region TEXT
)
''')

# Create sample data
products = ['Laptop', 'Phone', 'Tablet', 'Monitor']
regions = ['North', 'South', 'East', 'West']
start_date = datetime(2024, 1, 1)

sample_data = []
for i in range(100):  # 100 sample records
    date = start_date + timedelta(days=i % 30)
    for product in products:
        sample_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'product_name': product,
            'quantity': np.random.randint(1, 50),
            'unit_price': round(np.random.uniform(100, 1000), 2),
            'region': np.random.choice(regions)
        })

# Convert to DataFrame and save to SQLite
df = pd.DataFrame(sample_data)
df.to_sql('sales', conn, if_exists='replace', index=False)

conn.close() 