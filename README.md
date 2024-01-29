# Distributed Database Mini Project

**Description**

We are to create a distributed database system that will be able to handle the following:
1) Have the relations/tables on all 3 sites
2) Perform fragmentation
3) Perform reconstruction
4) Each site, according to the frequency of access, allocated a report.


**Requirements**

- 3 sites with three different participating database platforms
- At least 2 operating systems.
- At least 4 distributed relations
- Choose one of the sites to be the decision site and perform reconstruction using either views, functions, stored procedures or any other technique

**Distributed Relations:**
- Travellers
- Hotels
- Flights
- Bookings

**Site Structure:**
- Site A - where vertical fragmentation takes place. Runs on MacOS & MySQL
- Site B - where PHF takes place. Runs on Windows & MSSQL
- Site C - where DHF takes place. Runs on MacOS & PostgreSQL

## Running the App
-Clone this repository and navigate to its directory

-Run the following commands in the terminal

-Install relevant libraries using:
```bash
pip install mysql.connector
pip install pyscopg2
pip install pyodbc
```
-Simply run the files
```bash
python siteAmac.py
python siteBwindows.py
python siteCmac.py
```
