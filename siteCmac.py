import psycopg2
import pyodbc
from tabulate import tabulate 

# Initialize connection variables
postgres_connection = None
mssql_connection = None

# Connecting to MSSQL on Windows
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
    # Preparing a cursor object for MSSQL
    mssql_cursor = mssql_connection.cursor()

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

   
    print("")
    print("----------------------Vertical Fragmentation----------------------")
    print("")

    # Create fragment F1 which has flight details with the affinities A1 and A2(travellerID, flightName)
    print("F1 = Flight Details: flightID, travellerID, flightName FROM Flights: ")
    print("")
    Q1 = "SELECT flightID, travellerID, flightName FROM Flights"
    postgres_cursor.execute(Q1)
    Q1_result = postgres_cursor.fetchall()
    print(tabulate(Q1_result, headers=["flightID", "travellerID", "flightName"]))
    print("")

    # Create fragment F2 which has departure details with affinities A3, A4, A5(departureLocation, departureDate, departureTime)
    print("F2 = Departure Details: flightID, departureLocation, departureDate, departureTime FROM Flights:")
    print("")
    Q2 = "SELECT flightID, departureLocation, departureDate, departureTime FROM Flights"
    postgres_cursor.execute(Q2)
    Q2_result = postgres_cursor.fetchall()
    print(tabulate(Q2_result, headers=["flightID", "departureLocation", "departureDate", "departureTime"]))
    print("")

    # Create fragment F3 which has arrival details with affinities A6, A7 and A8(arrivalLocation, arrivalDate, arrivalTime)
    print("F3 = Arrival Details: flightID, arrivalLocation, arrivalDate, arrivalTime FROM Flights:")
    print("")
    Q3 = "SELECT flightID, arrivalLocation, arrivalDate, arrivalTime FROM Flights"
    postgres_cursor.execute(Q3)
    Q3_result = postgres_cursor.fetchall()
    print(tabulate(Q3_result, headers=["flightID", "arrivalLocation", "arrivalDate", "arrivalTime"]))
    print("")

# Close connections
if postgres_connection:
    postgres_cursor.close()
    postgres_cursor.close()

if mssql_connection:
    mssql_cursor.close()
    mssql_connection.close()