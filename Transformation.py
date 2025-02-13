import pandas as pd

# Load dataset
file_path = "Data/Amazon Sale Report.csv"  
df = pd.read_csv(file_path, low_memory=False)  # Suppress DtypeWarning

# Display basic dataset info
print("Original Dataset:")
print(df.head())
print(f"Total rows: {df.shape[0]}, Total columns: {df.shape[1]}")
print(df.info())

# 🔹 Step 1: Handle Missing Values
print("\nChecking for missing values...")
print(df.isnull().sum())

# Drop rows where more than 40% of values are missing
df.dropna(thresh=df.shape[1] * 0.6, inplace=True)

# Fill missing values
df["Amount"].fillna(df["Amount"].median(), inplace=True)  # Fill missing Amount with median
df["Category"].fillna("Unknown", inplace=True)  # Fill missing categories
df["Courier Status"].fillna("Unknown", inplace=True)  # Fill missing courier statuses

# 🔹 Step 2: Remove Duplicate Rows
print(f"\nDuplicate rows before removal: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
print(f"Duplicate rows after removal: {df.duplicated().sum()}")

# 🔹 Step 3: Format Data Types
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # Convert date column
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")  # Convert Amount to numeric
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")  # Convert Qty to numeric

# 🔹 Step 4: Handle Inconsistencies
df["Category"] = df["Category"].str.strip().str.title()  # Standardize category names

# Remove rows where Amount is 0 or negative
df = df[df["Amount"] > 0]

# 🔹 Step 5: Save the Cleaned Dataset
cleaned_file_path = "Amazon_Sale_Cleaned.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nData cleaning complete! Cleaned file saved as: {cleaned_file_path}")

# Final check
print("\nCleaned Dataset Sample:")
print(df.head())
print(f"Total cleaned rows: {df.shape[0]}, Total cleaned columns: {df.shape[1]}")
