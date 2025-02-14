# datafun-05-sql-project
This project integrates Python and SQL, focusing on database interactions using SQLite. The project involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Project Setup
## Step 1: Initialize Repository
1. Create a new GitHub repository named **datafun-05-sql** with a default `README.md`.
2. Clone the repository to your local machine in the **Projects** folder.
3. Open the project folder in **VS Code**.

## Essential Files

## Step 2: Add Key Files
1. **.gitignore**  
   Add a `.gitignore` file to specify files and folders to exclude from version control. You can reference an existing `.gitignore` template for Python projects.

2. **requirements.txt**  
   This file lists all necessary packages for the project. Review and adjust it to include or exclude packages based on your project’s needs.

3. **README.md**  
   Customize this file to provide an overview of the project, setup instructions, and usage details.

## Virtual Environment Setup

## Step 3: Create and Activate Virtual Environment
1. **Create a Virtual Environment:**

   ```Windows PowerShell
   python -m venv .venv

## Activate the Virtual Environment:
.\.venv\Scripts\activate

## Step 4: Install Required Packages
pip install -r requirements.txt

## Step 5: Select Python Interpreter in VS Code
1. Ensure VS Code is set to use the .venv environment.
2. Open the command palette using Ctrl + Shift + P.
3. Search for "Python: Select Interpreter".
4. Select the .venv folder located in the project root directory.

## Step 1: Create a New Database
1. Create a new SQLite database file (e.g., book_db.sqlite).

## Step 2: Create SQL Files
1. drop_tables.sql: Contains SQL statements to drop existing tables.
2. create_tables.sql: Contains SQL statements to create new tables.
3. insert_data.sql: Contains SQL statements to insert data into the tables.

## Step 3: Create Python Script
1. Write a Python script to execute the SQL statements from the files above. Example script name: db01_setup.py.
2. import sqlite3

## Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('book_db.sqlite')
cursor = conn.cursor()

## Function to execute SQL files
def execute_sql_file(filename):
    with open(filename, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

## Drop existing tables
Keep sql files in their own folder
execute_sql_file('drop_tables.sql')

## Create new tables
execute_sql_file('create_tables.sql')

## Insert data into tables
execute_sql_file('insert_data.sql')

## Commit changes and close connection
conn.commit()
conn.close()

## Step 4: Run the Python Script
py db01_setup.py
1. This command will execute the script, which will drop existing tables, create new ones, and insert the specified data into the database.

## Importing CSV Data into SQLite
## Prerequisites
- SQLite installed (`sqlite3.exe` in `C:\SQLite\`)
- CSV files (`authors.csv` and `books.csv`) stored in `data/` folder
- An SQLite database file (e.g., `csv_db.sqlite`)
---
### Open SQLite in VS Code Terminal and Run Below Commands
1. C:\SQLite\sqlite3.exe C:/projects/datafun-05-sql/csv_db.sqlite
2. .mode csv (Tells SQLite to expect CSV-formatted data)
3. .import C:/projects/datafun-05-sql/data/authors.csv Authors (imports this file data to db)
4. .import C:/projects/datafun-05-sql/data/books.csv Books (imports this file data to db)
5. Verify data uploaded by testing each: SELECT * FROM Authors LIMIT 5; SELECT * FROM Books LIMIT 5;
6. Open db is VS Code, if data isn't showing click refresh button, data should appear
7. To leave SQLite command: .exit

# Git Commands (FYI)
## Add Changes:
git add .

## Commit Changes:
git commit -m "Your commit message"

## Push Changes to GitHub:
git push -u origin main

## Pull Latest Changes:
git pull origin main