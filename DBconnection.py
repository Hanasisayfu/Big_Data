import psycopg2

# Database connection details
DB_NAME = "amazon_db"
DB_USER = "postgres"
DB_PASSWORD = "k1221"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
)
cur = conn.cursor()

# SQL script to create tables
create_tables_sql = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    customer_email VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    product_id INT REFERENCES products(product_id),
    customer_id INT REFERENCES customers(customer_id),
    quantity INT CHECK (quantity > 0),
    amount NUMERIC(10,2) CHECK (amount > 0)
);

CREATE TABLE IF NOT EXISTS shipment (
    shipment_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    courier_status VARCHAR(50),
    tracking_number VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS sentiment_analysis (
    review_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    sentiment_score FLOAT CHECK (sentiment_score BETWEEN 0 AND 1),
    review_text TEXT
);
"""

# Execute SQL script
cur.execute(create_tables_sql)
conn.commit()
cur.close()
conn.close()
print("Tables created successfully.")
