import sqlite3
import os

# Connect to SQLite database
conn = sqlite3.connect('pawradise_db.sqlite')
cursor = conn.cursor()

# Function to execute a SQL file and print results
def execute_query(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return
    
    try:
        with open(file_path, 'r') as file:
            queries = file.read().strip().split(';')
            
            for query in queries:
                query = query.strip()
                
                if query:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    
                    print(f"\nResults from {file_path}:\n")
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("(No results returned)")

    except sqlite3.Error as e:
        print(f"Error executing {file_path}: {e}")

# List of SQL query files
query_files = [
    "sql_queries/query_aggregation.sql",
    "sql_queries/query_filter.sql",
    "sql_queries/query_group_by.sql",
    "sql_queries/query_join.sql",
    "sql_queries/query_sorting.sql"
]

# Execute each query file
for file in query_files:
    print(f"\nRunning queries from: {file}")
    execute_query(file)

# Close database connection
conn.close()
