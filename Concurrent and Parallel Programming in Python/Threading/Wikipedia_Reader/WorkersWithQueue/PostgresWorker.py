import os
import threading

from sqlalchemy import create_engine
from sqlalchemy.sql import text

class PostgresMasterScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super(PostgresMasterScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue

    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break

        # symbol = val.get('symbol')
        # price = val.get('price')
        # extracted_time = val.get('extracted_time')
        symbol, price, extracted_time = val
        postgresWorker = PostgresWorker(symbol, price, extracted_time)
        postgresWorker.insert_into_db()

class PostgresWorker():
    def __init__(self, symbol, price, extracted_time):
        self.symbol = symbol
        self.price = price
        self.extracted_time = extracted_time

        self._PG_USER = os.environ.get('PG_USER') or 'postgres'
        self._PG_PW = os.environ.get('PG_PW') or ''
        self._PG_HOST = os.environ.get('PG_HOST') or 'localhost'
        self._PG_DB = os.environ.get('PG_DB') or 'postgres'

        self._engine = create_engine(f'postgresql://{self._PG_USER}:{self._PG_PW}@{self._PG_HOST}/{self._PG_DB}')

    def _create_insert_query(self):
        #SQL = f"""INSERT INTO prices (symbol, price, extracted_time) VALUES ({self.symbol}, {self.price}, {self.extracted_time})"""
        SQL = """INSERT INTO prices (symbol, price, extracted_time) VALUES (:symbol, :price, :extracted_time)"""
        return SQL

    def insert_into_db(self):
        insert_query = self._create_insert_query()

        with self._engine.connect() as conn:
            conn.execute(text(insert_query), {'symbol': self.symbol, 'price': self.price, 'extracted_time': self.extracted_time})
