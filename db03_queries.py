import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('pawradise_db.sqlite')
cursor = conn.cursor()

# Function to execute a SQL file and return a Pandas DataFrame
def execute_file_query(file_path):
    """Executes SQL queries from a file."""
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return None
    
    try:
        with open(file_path, 'r') as file:
            queries = file.read().strip().split(';')  # Split multiple SQL statements
            
            for query in queries:
                query = query.strip()
                if query:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description] 
                    df = pd.DataFrame(results, columns=columns)
                    
                    print(f"\nResults from {file_path}:\n")
                    print(df.to_string(index=False))  # Display as formatted table
                    
                    return df  # Return DataFrame for further processing

    except Exception as e:
        print(f"Error executing {file_path}: {e}")
        return None

# Function to execute a direct SQL query (for fetching dog ages)
def execute_sql_query(query):
    """Executes a direct SQL query and returns a Pandas DataFrame."""
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] 
        return pd.DataFrame(results, columns=columns)
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None

# List of SQL query files
query_files = [
    "sql_queries/query_aggregation.sql",
    "sql_queries/query_filter.sql",
    "sql_queries/query_group_by.sql",
    "sql_queries/query_join.sql",
    "sql_queries/query_sorting.sql"
]

# Store query results
dataframes = {}

# Execute each query file and store results
for file in query_files:
    print(f"\nRunning queries from: {file}")
    df = execute_file_query(file)
    if df is not None:
        dataframes[file] = df

# Fetch Dog Ages for Visualization using direct SQL
dog_ages_df = execute_sql_query("SELECT age FROM Dogs;")

# Close database connection
conn.close()

# 📊 **Plot: Number of Dogs Per Owner**
if "sql_queries/query_group_by.sql" in dataframes:
    df_grouped = dataframes["sql_queries/query_group_by.sql"]
    
    if "dog_count" in df_grouped.columns:
        plt.figure(figsize=(8, 5))
        plt.bar(df_grouped["owner_id"], df_grouped["dog_count"], color='skyblue')
        plt.xlabel("Owner ID")
        plt.ylabel("Number of Dogs")
        plt.title("Number of Dogs Per Owner")
        plt.xticks(rotation=45)
        plt.show()

# 📊 **Plot: Distribution of Dog Ages**
if dog_ages_df is not None and "age" in dog_ages_df.columns:
    plt.figure(figsize=(8, 5))
    dog_ages_df["age"].value_counts().sort_index().plot(kind="bar", color="green", edgecolor="black")
    plt.xlabel("Dog Age")
    plt.ylabel("Number of Dogs")
    plt.title("Number of Dogs in Each Age Group")
    plt.xticks(rotation=0)
    plt.show()

# 📊 **Plot: Histogram of Dog Ages**
if dog_ages_df is not None and "age" in dog_ages_df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(dog_ages_df["age"], bins=5, color="orange", edgecolor="black")
    plt.xlabel("Dog Age")
    plt.ylabel("Number of Dogs")
    plt.title("Distribution of Dog Ages")
    plt.show()

# 📊 **Plot: Average Dog Age Per Owner**
if "sql_queries/query_aggregation.sql" in dataframes:
    df_agg = dataframes["sql_queries/query_aggregation.sql"]

    if "avg_dog_age" in df_agg.columns:
        plt.figure(figsize=(8, 5))
        plt.hist(df_agg["avg_dog_age"], bins=5, color='purple', edgecolor='black')
        plt.xlabel("Average Age")
        plt.ylabel("Number of Owners")
        plt.title("Distribution of Average Dog Age")
        plt.show()