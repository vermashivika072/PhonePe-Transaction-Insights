import pandas as pd
import json
import os
from sqlalchemy import create_engine

# YOUR WORKING PASSWORD USE KARO
DB_USER = 'root'
DB_PASS = 'shivi@2604'
DB_HOST = '127.0.0.1'  # IP instead of localhost
DB_PORT = 3306
DB_NAME = 'phonepe_pulse'

print("🔄 Connecting to MySQL...")
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Test connection
try:
    engine.connect()
    print("✅ MySQL Connected!")
except:
    print("❌ Fix password first!")
    exit()

# Load ONLY essential data (5 min)
data_root = 'data'
folders = [
    ("aggregated/transaction/country/india/state", "aggregated_transaction"),
    ("map/transaction/country/india/state", "map_transaction")
]

for folder, table in folders:
    path = f"{data_root}/{folder}"
    if os.path.exists(path):
        print(f"Loading {path} -> {table}")
        file_count = 0
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    data = json.load(open(file_path))
                    df = pd.json_normalize(data['data']['data'])
                    df.to_sql(table, engine, if_exists='append', index=False)
                    file_count += 1
        print(f"✅ {table}: {file_count} files")
    else:
        print(f"❌ Folder missing: {path}")

print("🎉 Data Ready! Run: streamlit run streamlit/app.py")
