import pandas as pd

# Load the metadata.csv file from the data folder
df = pd.read_csv("metadata.csv")

# Display the first 5 rows of the DataFrame
print("📌 First 5 rows of the DataFrame:")
print(df.head())

# Display the column names and their data types
print("\n📌 Column names and their data types:")
print(df.info())

# Display basic statistical summary of numerical columns
print("\n📌 Basic statistical summary of numerical columns:")
print(df.describe())

# Display the number of rows and columns
print(f"\n📌 Number of rows: {df.shape[0]}")
print(f"📌 Number of columns: {df.shape[1]}")
# Explore the data