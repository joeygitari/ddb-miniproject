import mysql.connector
import psycopg2
from tabulate import tabulate 

# Initialize the connection variables
mysql_database_connection = None
local_stream = None

# Connecting to the MySQL database on the MAC machine
try:
    mysql_database_connection = mysql.connector.connect(
        host="192.168.0.102",
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
        host='192.168.0.102',
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


def init_fragment():    
    # Preparing a cursor object for the PostgreSQL database
    local_cursor = local_stream.cursor()
    local_stream.commit()   # Commit the changes to the database
    
    # Create fragment TravellersA18 where travellerAge > 18 on the PostgreSQL database
    a18_query = "SELECT * FROM Travellers WHERE travellerAge > 18"
    print("\n ")
    print("-----------Primary Horizontal Fragmentation-----------")
    print("\n ")
    print("a18 = SELECT * FROM Travellers WHERE travellerAge > 18")
    print(" ")
    local_cursor.execute(a18_query)
    a18 = local_cursor.fetchall()
    print(tabulate(a18, headers=["travellerID", "travellerName", "travellerAge", "travellerCountry"]))
    print("")

    # Create fragment TravellersU18 where travellerAge < 18 on the MySQL database
    cursorObject.execute("DROP TABLE IF EXISTS TravellersU18")
    cursorObject.execute("CREATE TABLE IF NOT EXISTS TravellersU18 (travellerID INT PRIMARY KEY, travellerName VARCHAR(50), travellerAge INT, travellerCountry VARCHAR(50));")
    print("u18 = SELECT * FROM Travellers WHERE travellerAge < 18") 
    print(" ")
    local_cursor = local_stream.cursor()
    u18_query = "SELECT * FROM Travellers WHERE travellerAge < 18"
    local_cursor.execute(u18_query)
    u18 = local_cursor.fetchall()
    print(tabulate(u18,headers=["travellerID", "travellerName", "travellerAge", "travellerCountry"]))
    # cursorObject.executemany("INSERT INTO TravellersU18 (travellerID INT PRIMARY KEY, travellerName VARCHAR(50), travellerAge INT, travellerCountry VARCHAR(50)VALUES (%s,%s,%s,%s);", u18)
    # Create view fragment_1 on the MySQL database
    cursorObject.execute("CREATE OR REPLACE VIEW fragment_1 AS SELECT travellerID, travellerName, travellerAge, travellerCountry FROM TravellersA18;")
    mysql_database_connection.commit()
    print("")

init_fragment()

def reconstruction():
    local_cursor = local_stream.cursor()
    print("Reconstruction from Derived Horizontal Fragmentation: ")
    print("")
    # Create table merged_dhf on the PostgreSQL database
    local_cursor.execute("DROP TABLE IF EXISTS merged_dhf")
    # local_cursor.execute("CREATE TABLE IF NOT EXISTS merged_dhf (hotelName VARCHAR(100), price DECIMAL(10,2), travellerAge) INT;")
    local_cursor.execute("CREATE TABLE IF NOT EXISTS merged_dhf (hotelName VARCHAR(100), price DECIMAL(10,2), travellerAge INT);")

    print("Query one: ")
    print(" ")
    # Check all the available tables in the Postgresql database
    print("All tables available in postgresql db: ")
    print(" ")
    local_cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    print(local_cursor.fetchall())

    # Reconstruction of Hybrid fragmentation. Schema Integration as we combine fragments from different databases

    # Display HotelsU18A300 from the PostgreSQL database
    query1 = "SELECT * FROM HotelsU18A300"
    local_cursor.execute(query1)
    query1_update = local_cursor.fetchall()
    print(" ")
    print("HotelsU18A300 table: (travellerAge < 18) && (price > 300)")
    print(tabulate(query1_update,headers=["hotelName","price"]))
    print("")

    #Display HotelsU18U300 from the PostgreSQL database
    query2 = "SELECT * FROM HotelsU18U300"
    local_cursor.execute(query2)
    query2_update = local_cursor.fetchall()
    print("HotelsU18U300 table: (travellerAge < 18) && (price < 300)")
    print(tabulate(query2_update,headers=["hotelName","price"]))
    print("")

    # #Doing reconstrcution of HotelsU18A300 and HotelsU18U300
    # Using UNION statement to perform reconstruction
    merge_query1 = "SELECT * FROM HotelsU18A300 UNION SELECT * FROM HotelsU18U300"
    local_cursor.execute(merge_query1)
    merge_update1 = local_cursor.fetchall()
    local_cursor.executemany("INSERT INTO merged_dhf (hotelName, price)VALUES (%s,%s);",merge_update1)
    local_stream.commit()
    print("Merged table: ) ")
    print(tabulate(merge_update1, headers=["hotelName", "price"]))
    print("")

     # Display HotelsA18A300 table from the MySQL database
    query3 = "SELECT * FROM HotelsA18A300"
    cursorObject.execute(query3)
    query3_update = cursorObject.fetchall()
    print("HotelsA18A300 table: (travellerAge > 18) && (price > 300)")
    print("")
    print(tabulate(query3_update, headers=["travellerAge", "price"]))
    print("")
    #Display HotelsA18U300 table from the MySQL database
    query4 = "SELECT * FROM HotelsA18U300"
    cursorObject.execute(query4)
    query4_update = cursorObject.fetchall()
    print("")
    print("HotelsA18U300 table: (travellerAge > 18) && (price < 300)")
    print("")
    print(tabulate(query4_update, headers=["hotelName", "price"]))
    print("")

    # Doing reconstrcution of dhf3 and dhf4
    # Using UNION statement to perform reconstruction
    merge_query2 = "SELECT * FROM HotelsA18A300 UNION SELECT * FROM HotelsA18U300"
    cursorObject.execute(merge_query2)
    merge_update2 = cursorObject.fetchall()
    local_cursor.executemany("INSERT INTO merged_dhf (hotelName, price)VALUES (%s,%s);",merge_update2)
    local_stream.commit()
    print("")
    print("Merged table: HotelsA18A300 && HotelsA18U300) ")
    print("")
    print(tabulate(merge_update2, headers=["hotelName","price"]))
    print("")

    # Display result of reconstruction
    merge_result = "SELECT * FROM merged_dhf"
    local_cursor.execute(merge_result)
    print("")
    final_merge = local_cursor.fetchall()
    print("Reconstructed table: HotelsA18A300 && HotelsA18U300 && HotelsU18A300 && HotelsU18U300) ")
    print("")
    print(tabulate(final_merge, headers=[]))
    print("")


reconstruction()