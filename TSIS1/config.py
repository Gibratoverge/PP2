import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="phonebook",
        user="postgres",
        password="2008"
    )
    print("OK CONNECTED")
except Exception as e:
    print(e)