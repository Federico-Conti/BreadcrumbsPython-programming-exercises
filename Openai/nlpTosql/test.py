import pandas as pd
from sqlalchemy import create_engine # db connection 
from sqlalchemy import text # text query

df = pd.read_csv("data/sales_data_sample.csv")
# df = df.groupby("QTR_ID").sum()["SALES"]
# print(df)

 # TEMPorary DB in RAM (not on disk)
 # PUSH Pandas DF --> TEMP DB
 # SQL qury on TEMP DB
 
strdb = "postgresql://postgres:3116@localhost:5433/postgres"
temp_db = create_engine(strdb,echo=False)

# Try to execute a simple SQL statement
# try:
#     with temp_db.connect() as connection:
#         result = connection.execute(text("SELECT 1"))
#         print("Connection successful.")
# except Exception as e:
#     print("Connection failed:", e)

try:
 data = df.to_sql(name="Sales",con=temp_db, if_exists='fail') # con := connectionDbName
 print(data)
except Exception as e:
    print("Sales already eixist")

print(f"database string: {temp_db}")
with temp_db.connect() as conn:
    # makes the connection
    # run code indentation/block
    result = conn.execute(text("SELECT * FROM \"Sales\""))
    # auto close connection
print(result.all())
