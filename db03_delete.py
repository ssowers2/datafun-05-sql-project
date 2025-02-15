import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('pawradise_db.sqlite')
cursor = conn.cursor()

try:
    # Read and execute the update SQL file
    with open('sql_features/delete_records.sql', 'r') as file:
        cursor.executescript(file.read())

    # Commit the changes
    conn.commit()
    print("Record deletion was successful!")

except Exception as e:
    print(f"Error deleting records: {e}")

finally:
    # Close the connection
    conn.close()