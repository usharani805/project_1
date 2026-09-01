from connection import get_connection


connection = get_connection()

with open("schema.sql", "r") as file:
    sql = file.read()

with connection.cursor() as cursor:
    cursor.execute(sql)

connection.commit()
connection.close()

print("Tables created successfully!")