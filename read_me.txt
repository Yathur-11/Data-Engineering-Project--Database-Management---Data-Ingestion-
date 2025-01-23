Data Engineering Project: Database Management & Data Ingestion

Overview:-
This project involves working with wealth-related data sourced from Kaggle. The goal was to design and implement a PostgreSQL database, process the provided CSV data using pandas, and efficiently load it into the database. This project demonstrates skills in database design, data processing, and SQL.

Key Features
Database Creation: Used psycopg2 to connect to PostgreSQL and create a new database.

Data Processing: Cleaned and processed CSV files (Wealth-AccountsCountry.csv, Wealth-AccountData.csv, Wealth-AccountSeries.csv) using pandas.

Table Design: Designed and created 3 SQL tables: accountsdata, accountscountry, and accountseries in PostgreSQL.

Data Insertion: Utilized parameterized SQL queries to insert data into the database while maintaining data integrity.

Technologies Used:-
PostgreSQL: Relational database management system.
psycopg2: Python library to connect and interact with PostgreSQL.
pandas: Python library for data manipulation and cleaning.
SQL: Database design and querying.

Steps Performed
Created a new PostgreSQL database.
Loaded and processed data from Kaggle datasets. (I've provided it inside the repository)
Designed tables to store data efficiently.
Inserted data into PostgreSQL using parameterized queries.
Managed transactions to ensure data integrity.

Installation & Setup
Install psycopg2 and pandas:
bash
Copy
Edit
pip install psycopg2 pandas
Set up PostgreSQL and create a new database (accounts15):

python
Copy
Edit
conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=root")
cur = conn.cursor()
cur.execute("CREATE DATABASE accounts15")
conn.close()
Upload the CSV files from Kaggle into the project directory.

Run the provided code to create the database tables and insert the data.

Future Improvements :- 

Data validation and cleaning improvements.
Automate the data loading process using an ETL pipeline.
Data analysis and visualization using the loaded data.
