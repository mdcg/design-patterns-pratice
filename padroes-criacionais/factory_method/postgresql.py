from contextlib import suppress

import psycopg2

from factory import Database, Tester


class PostgreSQL(Database):
    def connect(self):
        return psycopg2.connect(
            dbname=self.config.database,
            user=self.config.username,
            password=self.config.password,
            host=self.config.host,
            port=self.config.port,
        )

    def sanity_sake(self):
        response = False
        with suppress(psycopg2.OperationalError):
            cur = self.conn.cursor()
            cur.execute("SELECT 1")
            response = True

        return response


class PostgreSQLTester(Tester):
    def __init__(self, config):
        super().__init__(config)
        self.pg_con = PostgreSQL(self.config)

    def connection(self):
        return self.pg_con
