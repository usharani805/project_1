import psycopg2


def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="Employee_db",
        user="postgres",
        password="Usha@222"
    )

    return connection