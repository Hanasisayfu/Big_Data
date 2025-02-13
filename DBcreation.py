import psycopg2

DB_USER = "postgres"  # Change to your PostgreSQL username
DB_PASSWORD = "k1221"  # Change to your password
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Connect to PostgreSQL (without specifying a database)
    conn = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    conn.autocommit = True  # Allow database creation
    cur = conn.cursor()

    # Create database
    cur.execute("CREATE DATABASE amazon_db;")
    print("✅ Database 'amazon_db' created successfully!")

    # Close connection
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("❌ Error creating database:", e)
