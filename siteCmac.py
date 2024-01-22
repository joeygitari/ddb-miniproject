import psycopg2
import pyodbc

# Initialize connection variables
postgres_connection = None
mssql_connection = None

# Connecting to PostgresSQL on Mac
try:
    postgres_connection = psycopg2.connect(
        host='localhost',
        port='5432',
        database='ddb-miniproject',
        user='joeygitari',
        password=''
    )

    print("Connected to PostgresSQL database successfully.")
except psycopg2.Error as err:
    print(f"PostgresQL Connection Error: {err}")

# Check if the connection was successful before proceeding
if postgres_connection:
    # Preparing a cursor object for PostgresSQL
    postgres_cursor = postgres_connection.cursor()

# Connecting to MSSQL on Windows
try:
    mssql_connection = pyodbc.connect(
        driver='{ODBC Driver 17 for SQL Server}',
        server='moh.mshome.net',
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
    # Preparing a cursor object for MSSQL
    mssql_cursor = mssql_connection.cursor()
