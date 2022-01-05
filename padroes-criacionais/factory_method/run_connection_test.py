from time import sleep

from config import get_config
from mysql import MySQLTester
from postgresql import PostgreSQLTester


def main():
    DATABASES = {
        "postgresql": PostgreSQLTester,
        "mysql": MySQLTester,
    }

    database_config = get_config()
    database_type = database_config.type

    try:
        database_tester = DATABASES[database_type](database_config)
    except KeyError:
        print("Not implemented database connection test.")

    while response := database_tester.test():
        print(f"{response} - Waiting for another database connection test...")
        sleep(5)
    else:
        print(f"Connection closed.")


if __name__ == "__main__":
    main()
