import openai
import os
import pandas as pd
import logging
import dbsetup
import prompt
import json
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

load_dotenv("../.env")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_version = "2022-12-01"

if __name__ == "__main__":
    logging.info("Loading data...")
    df = pd.read_csv("data/sales_data_sample.csv")
    logging.info(f"Data Format: {df.shape}")

    logging.info("Converting to database...")
    database = dbsetup.dataframe_to_database(df, "Sales")
   
    fixed_sql_prompt = prompt.create_table_definition_prompt(df, "Sales")
    logging.info(f"Fixed SQL Prompt: {fixed_sql_prompt}")

    logging.info("Waiting for user input...") # Exalmple: return a sum of SALES per POSTALCODE
    user_input = prompt.user_query_input()
    final_prompt = prompt.combine_prompts(fixed_sql_prompt, user_input)
    logging.info(f"Final Prompt: \n{final_prompt}")

    logging.info("Sending to OpenAI...")
    response = prompt.send_to_openai(final_prompt)
    
    # Convert the response to a dictionary
    response_dict = response.model_dump() 
    # Save the response to a JSON file
    with open('response.json', 'w') as f:
        json.dump(response_dict, f)
    
    response = response.model_dump()
    proposed_query = response["choices"][0]["text"]
    logging.info(f"OnepAi completition response: \n{proposed_query}")
     
    proposed_query_postprocessed = dbsetup.handle_response(proposed_query)
    logging.info(f"Response obtained. Proposed sql query: {proposed_query_postprocessed}")
  
    
    result = dbsetup.execute_query(database, proposed_query_postprocessed)
    logging.info(f"Result: {result}")
    print(result)
    
