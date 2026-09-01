import psycopg


def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="Employee_db",
        user="postgres",
        password="Usha@222",
        connect_timeout=5
    )
    return connection