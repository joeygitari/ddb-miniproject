import pyodbc
import mysql.connector

# Connecting to the MySQL database on MacOS
mysql_connection = mysql.connector.connect(
    host="192.168.100.9",
    port="3306",
    user="root",
    passwd="",
    database="ddb-miniproject"
)

# Preparing a cursor object for the MySQL database
mysql_cursor = mysql_connection.cursor(buffered=True)

# Connecting to the MSSQL database on Windows
mssql_connection = pyodbc.connect(
    driver='{ODBC Driver 17 for SQL Server}', 
    server='Moh',
    database='ddb-miniproject',
    user='root',
    password='',
    trusted_connection='yes'
)

# Preparing a cursor object for the MSSQL database
mssql_cursor = mssql_connection.cursor()