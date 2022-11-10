import psycopg2
from self import self


# Sample class with init method
class Database:
    def __init__(self):
        self.dbName = "postgress_dbname"
        self.dbUser = "postgress_user"
        self.dbPassword = "55555555555"
        self.dbHost = "100.250.250.200"
        self.dbPort = "599992"
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
