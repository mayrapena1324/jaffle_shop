import pandas as pd

def model(dbt, session):
    # Load data from the source orders table
    source_orders_df = dbt.ref("stg_orders")

    # Convert 'order_date' from string to datetime
    source_orders_df['order_date'] = pd.to_datetime(source_orders_df['order_date'], format='%Y-%m-%d %H:%M:%S')

    # Add a new column 'days_since_order' calculating the number of days from 'order_date' to today
    source_orders_df['days_since_order'] = (pd.Timestamp('now') - source_orders_df['order_date']).dt.days

    # Clean 'status' by capitalizing and stripping white spaces
    source_orders_df['status'] = source_orders_df['status'].str.upper().str.strip()

    return source_orders_df
