import psycopg2
from self import self


# Sample class with init method
class Database:
    def __init__(self):
        self.dbName = "connectips"
        self.dbUser = "postgres"
        self.dbPassword = "123456"
        self.dbHost = "10.250.3.20"
        self.dbPort = "5432"
        self._conn = psycopg2.connect(database=self.dbName, user=self.dbName,
                                password=self.dbPassword, host=self.dbHost, port=self.dbPort)
        print('Connected to DB:', self._conn)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
