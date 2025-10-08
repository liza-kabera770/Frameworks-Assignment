# Step 1: Import libraries
import pandas as pd

# Step 2: Load the dataset
data = pd.read_csv("metadata.csv", low_memory=False)

# Step 3: Look at the first few rows
print("✅ First 5 rows of the dataset:")
print(data.head())

# Step 4: Check the shape (rows, columns)
print("\n📏 Dataset dimensions:")
print(data.shape)

# Step 5: Check data types
print("\n🧩 Column data types:")
print(data.dtypes)

# Step 6: Check missing values in important columns
print("\n🔍 Missing values in important columns:")
print(data[['title', 'abstract', 'publish_time', 'journal']].isnull().sum())

# Step 7: Basic stats for numeric columns
print("\n📊 Basic statistics for numeric columns:")
print(data.describe())