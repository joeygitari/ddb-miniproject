import pyodbc
import mysql.connector
from tabulate import tabulate 

# Initialize connection variables
mysql_connection = None
mssql_connection = None

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
    
    print("")
    print("-----------Primary Horizontal Fragmentation-----------") 
    print("")
    # Step 1: Perform PHF on the Travellers table
    # Query to create fragment TravellersA18 WHERE [travellerAge > 18] ";
    mysql_cursor.execute("DROP TABLE IF EXISTS TravellersA18")
    mysql_cursor.execute("CREATE TABLE IF NOT EXISTS TravellersA18 (SELECT * FROM Travellers WHERE travellerAge > 18)")
    mysql_cursor.execute("SELECT * FROM TravellersA18")
    a18_result = mysql_cursor.fetchall()
    print("TravellersA18: travellerAge > 18' : ")
    print("")
    print(tabulate(a18_result, headers=["travellerID", "travellerName", "travellerAge", "travellerCountry"]))
    print("")

    mysql_cursor.execute("DROP TABLE IF EXISTS TravellersU18")
    mysql_cursor.execute("CREATE TABLE IF NOT EXISTS TravellersU18 (SELECT * FROM Travellers WHERE travellerAge < 18)")
    mysql_cursor.execute("SELECT * FROM TravellersU18")
    u18_result = mysql_cursor.fetchall()
    print("TravellersU18: travellerAge < 18' : ")
    print("")
    print(tabulate(u18_result, headers=["travellerID", "travellerName", "travellerAge", "travellerCountry"]))
    print("")

    print("")
    print("-----------Derived Horizontal Fragmentation-----------") 
    print("")
    # Step 2: Perform DHF on the Hotels table. Keep HotelsA300 and HotelsU300 in same site A
    mysql_cursor.execute("DROP TABLE IF EXISTS HotelsA18A300")
    mysql_cursor.execute("CREATE TABLE IF NOT EXISTS HotelsA18A300 (SELECT Hotels.hotelName, Hotels.price FROM Hotels INNER JOIN TravellersA18 ON TravellersA18.travellerID = Hotels.travellerID WHERE Hotels.price > 300);")
    mysql_cursor.execute("SELECT * FROM HotelsA18A300")
    a300_result = mysql_cursor.fetchall()
    print("HotelsA18A300: Hotels with price > 300 x TravellerA18:")
    print("")
    print(tabulate(a300_result, headers=["hotelName", "price"]))
    print("")

    mysql_cursor.execute("DROP TABLE IF EXISTS HotelsA18U300")
    mysql_cursor.execute("CREATE TABLE IF NOT EXISTS HotelsA18U300 (SELECT Hotels.hotelName, Hotels.price FROM Hotels INNER JOIN TravellersA18 ON TravellersA18.travellerID = Hotels.travellerID WHERE Hotels.price < 300);")
    mysql_cursor.execute("SELECT * FROM HotelsA18U300")
    u300_result = mysql_cursor.fetchall()
    print("HotelsA18U300: Hotels with price < 300 x TravellerA18: ")
    print("")
    print(tabulate(u300_result, headers=["hotelName", "price"]))
    print("")
    #End

    mysql_cursor.execute("DROP TABLE IF EXISTS HotelsU18A300")
    mysql_cursor.execute("CREATE TABLE IF NOT EXISTS HotelsU18A300 (SELECT Hotels.hotelName, Hotels.price FROM Hotels INNER JOIN TravellersU18 ON TravellersU18.travellerID = Hotels.travellerID WHERE Hotels.price < 300);")
    mysql_cursor.execute("SELECT * FROM HotelsU18A300")
    a300_result = mysql_cursor.fetchall()
    print("HotelsU18A300: Hotels with price < 300 x TravellerU18:")
    print("")
    print(tabulate(a300_result, headers=["hotelName", "price"]))
    print("")

    mysql_cursor.execute("DROP TABLE IF EXISTS HotelsU18U300")
    mysql_cursor.execute("CREATE TABLE IF NOT EXISTS HotelsU18U300 (SELECT Hotels.hotelName, Hotels.price FROM Hotels INNER JOIN TravellersU18 ON TravellersU18.travellerID = Hotels.travellerID WHERE Hotels.price < 300);")
    mysql_cursor.execute("SELECT * FROM HotelsU18U300")
    u300_result = mysql_cursor.fetchall()
    print("HotelsU18U300: Hotels with price < 300 x TravellerU18: ")
    print("")
    print(tabulate(u300_result, headers=["hotelName", "price"]))
    print("")
    #End

# Close connections
if mysql_connection:
    mysql_cursor.close()
    mysql_connection.close()

if mssql_connection:
    mssql_cursor.close()
    mssql_connection.close()