import os
import sys
from src.mlproject.exceptions import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading  mysql database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection etabilished {mydb}")
        
        df=pd.read_sql_query('select * from students', mydb)
        print(df.head())
        
        return df
        
    except Exception as e:
        logging.error(f"Error reading from MySQL: {e}")
        raise CustomException(e, sys)