import mysql.connector

from factory import Database, Tester


class MySQL(Database):
    def connect(self):
        return mysql.connector.connect(
            database=self.config.database,
            user=self.config.username,
            password=self.config.password,
            host=self.config.host,
            port=self.config.port,
        )

    def sanity_sake(self):
        return self.conn.is_connected()


class MySQLTester(Tester):
    def __init__(self, config):
        super().__init__(config)
        self.mysql_con = MySQL(self.config)

    def connection(self):
        return self.mysql_con
