import pandas as pd
import psycopg2
from sqlalchemy import create_engine


# Load cleaned transformed dataset
df = pd.read_csv("transformed_sales_data.csv")  


# Step 2: Connect to Data Warehouse - Example: PostgreSQL
engine = create_engine("postgresql://user:password@localhost:5432/datawarehouse")


# Step 3: Load data into target table
df.to_sql(
    name="sales_fact",     # Target table name
    con=engine,
    if_exists="append",    # Load mode - append if data exist or 'replace', or 'fail'
    index=False
)

print("✅ Data successfully loaded into the data warehouse!")
