import os
from sqlalchemy import create_engine
import pandas as pd

class db_helper:

   def connect_pg_db(self, database_name, username, password, host, port = 5432):
      url = "postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, database_name)
      engine = create_engine(url)
      yield engine

   def connect_mysql_db(self, database_name, username, password, host, port = 3306):
      engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database_name}')
      yield engine

   def create_table_ddl(self, csv_file_name, engine):
      df = pd.read_csv(csv_file_name, nrows = 100)
      schema = pd.io.sql.get_schema(df, name = '', con=engine)
      yield schema

   def 