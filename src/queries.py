import pandas as pd
from sqlalchemy import create_engine

DB_USER = 'root'
DB_PASS = 'your_password'
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@localhost/phonepe_pulse')

def get_top_states(year=2023, quarter=1):
    query = """
    SELECT state, SUM(transaction_count) as total_count, SUM(total_amount)/1e9 as total_amount_cr
    FROM aggregated_transaction 
    WHERE year=%s AND quarter=%s
    GROUP BY state ORDER BY total_count DESC LIMIT 10
    """
    return pd.read_sql(query, engine, params=(year, quarter))

def get_transaction_by_type(year=2023, quarter=1):
    query = """
    SELECT transaction_type, SUM(transaction_count) as count, SUM(total_amount)/1e9 as amount_cr
    FROM aggregated_transaction 
    WHERE year=%s AND quarter=%s
    GROUP BY transaction_type ORDER BY count DESC
    """
    return pd.read_sql(query, engine, params=(year, quarter))

def get_top_districts(state='maharashtra', year=2023, quarter=1):
    query = """
    SELECT district, SUM(transaction_count) as total_count
    FROM map_transaction 
    WHERE state=%s AND year=%s AND quarter=%s
    GROUP BY district ORDER BY total_count DESC LIMIT 10
    """
    return pd.read_sql(query, engine, params=(state, year, quarter))
