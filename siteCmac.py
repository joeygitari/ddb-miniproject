import psycopg2
import pyodbc

# Connecting to PostgreSQL on Mac
postgres_connection = psycopg2.connect(
    host='192.168.100.9',
    port='5432',
    database='ddb-miniproject',
    user='joeygitari',
    password=''
)

# Preparing a cursor object for PostgreSQL
postgres_cursor = postgres_connection.cursor()

# Connecting to MSSQL on Windows
mssql_connection = pyodbc.connect(
    driver='{ODBC Driver 17 for SQL Server}', 
    server='Moh',
    database='ddb-miniproject',
    user='root',
    password='',
    trusted_connection='yes'
)

# Preparing a cursor object for MSSQL
mssql_cursor = mssql_connection.cursor()