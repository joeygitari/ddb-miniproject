import mysql.connector
import psycopg2

# Initialize the connection variables
mysql_database_connection = None
local_stream = None

# Connecting to the MySQL database on the MAC machine
try:
    mysql_database_connection = mysql.connector.connect(
        host="192.168.100.9",
        port="3306",
        user="root",
        passwd="",
        database="ddb-miniproject")

    print("Connected to MySQL database successfully.")
except mysql.connector.Error as err:
    print(f"MySQL Connection Error: {err}")

# Check if the connection was successful before proceeding
if mysql_database_connection:
    # preparing a cursor object for the MySQL database
    cursorObject = mysql_database_connection.cursor(buffered=True)

# connecting to the PostgresSQL database on the MAC machine
try:
    local_stream = psycopg2.connect(
        host='192.168.100.9',
        port='5432',
        database='ddb-miniproject',
        user='joeygitari',
        password='')

    print("Connected to PostgresSQL database successfully.")
except psycopg2.Error as err:
    print(f"PostgresSQL Connection Error: {err}")

# Check if the connection was successful before proceeding
if local_stream:
    # preparing a cursor object for the PostgresSQL database
    local_cursor = local_stream.cursor()
