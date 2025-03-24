import pandas as pd

# Load raw data
df = pd.read_csv('data/raw/sales_data.csv')

# Initial Data Inspection 
print("Initial Data Inspection:")
df.info()          # Check data types and missing values
print("\nSummary Statistics:")
print(df.describe()) 
print("\nFirst 5 Rows of Data:")
print(df.head())      # Inspect the first few rows
print("\nRandom Sample of Data:")
print(df.sample(5))   


# Handle Missing Data
print("\nMissing Data Check:")
print(df.isnull().sum()) 

# Fill missing values
df = df.fillna('N/A')  

# Handle SaleDate Format
print("\nStandardizing SaleDate Format:")
df['SaleDate'] = pd.to_datetime(df['SaleDate'], errors='coerce')  # Convert SaleDate to datetime

# Handle SaleAmount (Ensure non-negative SaleAmount)
print("\nChecking SaleAmount for Outliers:")
df['SaleAmount'] = df['SaleAmount'].apply(lambda x: x if x >= 0 else 0)  

# Drop rows with DiscountPercent outside the valid range [0, 1]
df = df[(df['DiscountPercent'] >= 0) & (df['DiscountPercent'] <= 1)]

# Handle State Inconsistencies 
print("\nStandardizing State Column:")
df['State'] = df['State'].str.strip().str.lower()  # Convert state names to lowercase and strip any whitespaces

# Drop duplicates based on all columns except 'TransactionID', keeping only the first occurrence
df_cleaned = df.drop_duplicates(subset=df.columns.difference(['TransactionID']).tolist(), keep=False)

# Check the number of remaining duplicates
print(f"Remaining duplicates after removal: {df_cleaned.duplicated().sum()}")

# Final Quality Checks
print("\nFinal Quality Check:")
df_cleaned.info() 
print("\nCleaned Data Head:")
print(df_cleaned.head()) 

# Save cleaned data
df_cleaned.to_csv('data/prepared/sales_data_prepared.csv', index=False)

print("Data cleaned and saved to 'data/prepared/sales_data_prepared.csv'")
