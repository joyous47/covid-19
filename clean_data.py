import pandas as pd
import re

# Load the metadata.csv file
df = pd.read_csv("metadata.csv", low_memory=False)

# -----------------------------
# Clean malformed data
# -----------------------------
# Fix malformed dates with extra spaces
df["publish_time"] = df["publish_time"].str.strip().str.replace(r'\s+', '-', regex=True)

# Fix malformed author names with extra spaces
df["authors"] = df["authors"].str.replace(r'\s+', ' ', regex=True).str.strip()

# Fix malformed journal names with extra spaces
df["journal"] = df["journal"].str.replace(r'\s+', ' ', regex=True).str.strip()

# -----------------------------
# Handle missing values in key columns
# -----------------------------
df["title"].fillna("No Title", inplace=True)
df["abstract"].fillna("No Abstract", inplace=True)
df["authors"].fillna("Unknown", inplace=True)
df["journal"].fillna("Unknown", inplace=True)
df["source_x"].fillna("Unknown", inplace=True)

# Drop rows where publish_time is missing
df.dropna(subset=["publish_time"], inplace=True)

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Drop rows where conversion failed
df.dropna(subset=["publish_time"], inplace=True)

# Extract publication year
df['publish_year'] = df['publish_time'].dt.year

# Add a simple feature: abstract word count
df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))

# -----------------------------
# Preview
# -----------------------------
print("✅ First 5 rows of cleaned DataFrame:")
print(df.head())

print("\n✅ Column names and types after cleaning:")
print(df.info())

# Save cleaned dataset
df.to_csv("metadata_cleaned.csv", index=False)
print("\n✅ Cleaned data saved to metadata_cleaned.csv")