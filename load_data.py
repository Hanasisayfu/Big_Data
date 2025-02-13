import pandas as pd
import psycopg2

# Define file path
file_path = "Amazon_Sale_Cleaned.csv"

# Step 1: Load the CSV file
df = pd.read_csv(file_path, low_memory=False)  # Avoid mixed types warning

# Print the column names to check if 'Product Name' exists
print("🔹 Column names in CSV file:")
print(df.columns)

# Step 2: Clean column names by stripping any leading/trailing spaces
df.columns = df.columns.str.strip()  # Remove spaces from column names

# Step 3: Check if 'Product Name' exists in the columns
if 'Product Name' not in df.columns:
    # Print the columns for debugging purposes
    print("❌ 'Product Name' not found! Please verify column names.")
    print("Available columns:")
    print(df.columns)
    
    # Optionally, use a different column as 'Product Name'
    # Use 'SKU' or 'Style' as 'Product Name'
    if 'SKU' in df.columns:
        df.rename(columns={'SKU': 'Product Name'}, inplace=True)
    elif 'Style' in df.columns:
        df.rename(columns={'Style': 'Product Name'}, inplace=True)
    else:
        print("❌ No suitable column found to rename as 'Product Name'.")
        # Handle the error, maybe by exiting or using a placeholder column
        exit()
else:
    print("✅ 'Product Name' column found!")

# Step 4: Handle mixed data types if necessary
# If there are columns with mixed data types (e.g., 'Amount'), specify dtype
# Example:
# df = pd.read_csv(file_path, dtype={'Amount': str}, low_memory=False)

# Step 5: Connect to PostgreSQL
try:
    connection = psycopg2.connect(
        host="Localhost",
        port="5432",
        dbname="amazon_db",
        user="postgres",
        password="k1221"
    )
    cursor = connection.cursor()
    print("✅ Connected to PostgreSQL successfully!")
    
    # Insert data into PostgreSQL (adjust as necessary)
    for index, row in df.iterrows():
        cursor.execute(""" 
            INSERT INTO your_table (Product_Name, Category, Size, Amount, Status, Date, ...) 
            VALUES (%s, %s, %s, %s, %s, %s, ...) 
        """, (row['Product Name'], row['Category'], row['Size'], row['Amount'], row['Status'], row['Date'], ...))
    
    # Commit changes
    connection.commit()
    print("✅ Data inserted into PostgreSQL.")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("🔹 PostgreSQL connection closed.")
