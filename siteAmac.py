import pyodbc
import mysql.connector

# Initialize connection variables
mysql_connection = None
mssql_connection = None

# Connecting to the MySQL database on MacOS
try:
    mysql_connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        passwd="",
        database="ddb-miniproject"
    )

    print("Connected to MySQL database successfully.")
except mysql.connector.Error as err:
    print(f"MySQL Connection Error: {err}")

# Check if the connection was successful before proceeding
if mysql_connection:
    # Preparing a cursor object for the MySQL database
    mysql_cursor = mysql_connection.cursor(buffered=True)

# Connecting to the MSSQL database on Windows
try:
    mssql_connection = pyodbc.connect(
        driver='{ODBC Driver 17 for SQL Server}',
        server='192.168.0.117',
        database='ddb-miniproject',
        user='joeygitari',
        password='pookie',
        trusted_connection='no'
    )

    print("Connected to MSSQL database successfully.")
except pyodbc.Error as err:
    print(f"MSSQL Connection Error: {err}")

# Check if the connection was successful before proceeding
if mssql_connection:
    # Preparing a cursor object for the MSSQL database
    mssql_cursor = mssql_connection.cursor()

