import os
from sqlalchemy import create_engine, MetaData

class Database():
    
    def __init__(self):

        self.engine = create_engine(f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}")
        self.conn = self.engine.connect()
        self.meta_data = MetaData(bind=self.conn)
        self.add_data = []
        self.table_names = self.engine.table_names()

    def add(self, table, data):
        """Add data to Postgres Database
        Args:
            data (List[List]): Data to add
        """
        query=f"INSERT INTO {table} VALUES(%s,%s, %s, %s)"
        for d in data :
            self.add_data.append(tuple(d))
        self.conn.execute(query,self.add_data)
        self.add_data = []

    def read(self, table):
        """Read information from Postgres database

                Returns:
            data: data stored in Postgres database
        """
        data = self.conn.execute(f"SELECT * FROM {table}").fetchall()
        return data