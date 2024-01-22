import pandas as pd
import psycopg2  
from sqlalchemy import create_engine # db connection
from sqlalchemy import text # text query
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def dataframe_to_database(df, table_name):
    """Convert a pandas dataframe to a database.
        Args:
            df (dataframe): pd.DataFrame which is to be converted to a database
            table_name (string): Name of the table within the database
        Returns:
            engine: SQLAlchemy engine object
    """
    engine = create_engine(f'postgresql://postgres:{os.getenv("DB_PASSWORD")}@localhost:5433/postgres')
    try:
     df.to_sql(name=table_name, con=engine, index=False ,if_exists='fail')
     return engine
    except Exception as e:
     print("Sales already eixist")
     return engine
    

def handle_response(response):
    """Handles the response from OpenAI.

    Args:
        response (openAi response): Response json from OpenAI

    Returns:
        string: Proposed SQL query
    """
        
    # response = response.model_dump()
    # query = response["choices"][0]["text"]
    query = response
    if query.startswith(" "):
        query = "Select"+ query
    return query

def execute_query(engine, query):
    """Execute a query on a database.

    Args:
        engine (SQLAlchemy engine object): database engine
        query (string): SQL query

    Returns:
        list: List of tuples containing the result of the query
    """
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()
    
    # engine.autocommit = True
    # cursor = engine.cursor() 
    # query = """
    #  SELECT * FROM sales
    # """
    # cursor.execute(query) 
    # engine.commit() 
    # engine.close()
    # return cursor.fetchall() 
 
    
    