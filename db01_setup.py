import sqlite3

# Connect to the SQLite database (creates the file if it doesn’t exist)
conn = sqlite3.connect('pawradise_db.sqlite')
cursor = conn.cursor()

# Drop existing tables (if they exist) to reset the database
with open('sql_statements/01_drop_tables.sql', 'r') as file:
    cursor.executescript(file.read())

# Create new tables based on the schema
with open('sql_statements/02_create_tables.sql', 'r') as file:
    cursor.executescript(file.read())

# Insert initial data into the tables
with open('sql_statements/03_insert_records.sql', 'r') as file:
    cursor.executescript(file.read())

# Save (commit) the changes to the database
conn.commit()

# Close the database connection
conn.close()

# Print confirmation message
print('The database and tables were created successfully!')