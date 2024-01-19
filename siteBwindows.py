import mysql.connector
import psycopg2

# Connecting to the MySQL database on the MAC machine
mysql_database_connection = mysql.connector.connect(
    host="192.168.100.9",
    port="3306",
    user="root",
    passwd="",
    database="ddb-miniproject")

# preparing a cursor object for the MySQL database
cursorObject = mysql_database_connection.cursor(buffered=True)

# connecting to the PostgresSQL database on the MAC machine
local_stream = psycopg2.connect(
    host='192.168.100.9',
    port='5432',
    database='ddb-miniproject',
    user='',
    password=''
)

