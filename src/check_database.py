import sqlite3
import pandas as pd

def check_database():
    try:
        # Connect to database
        conn = sqlite3.connect('database/sales.db')
        
        # Check if table exists and get row count
        row_count = pd.read_sql_query("SELECT COUNT(*) as count FROM sales", conn).iloc[0]['count']
        print(f"✓ Database connected successfully")
        print(f"✓ Found {row_count} records in sales table")
        
        # Show first few records
        print("\nFirst 5 records in database:")
        sample_data = pd.read_sql_query("SELECT * FROM sales LIMIT 5", conn)
        print(sample_data)
        
        conn.close()
        return True
        
    except sqlite3.OperationalError as e:
        print("✗ Error: Database or table not found")
        print(f"Error details: {str(e)}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    check_database() 