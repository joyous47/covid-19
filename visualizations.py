import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# === Load data ===
df = pd.read_csv("metadata_cleaned.csv")
df.columns = df.columns.str.strip()
df['publish_year'] = df['publish_year'].astype(int)
df['authors'] = df['authors'].fillna("Unknown")
df['journal'] = df['journal'].fillna("Unknown")

# === Publications per year ===
plt.figure(figsize=(12, 6))
year_counts = df['publish_year'].value_counts().sort_index()
sns.barplot(x=year_counts.index, y=year_counts.values, palette='viridis')
plt.title('Number of Publications per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/publications_per_year.png')
plt.close()

# === Top 10 journals ===
top_journals = df['journal'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='magma')
plt.title('Top 10 Journals by Publication Count')
plt.xlabel('Number of Publications')
plt.ylabel('Journal')
plt.tight_layout()
plt.savefig('images/top_journals.png')
plt.close()

# === Top 10 authors ===
top_authors = df['authors'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_authors.values, y=top_authors.index, palette='plasma')
plt.title('Top 10 Authors by Publication Count')
plt.xlabel('Number of Publications')
plt.ylabel('Author')
plt.tight_layout()
plt.savefig('images/top_authors.png')
plt.close()

print("✅ Visualizations saved to images/ folder")