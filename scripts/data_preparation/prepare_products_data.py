import pandas as pd

# Load raw data
df = pd.read_csv('data/raw/products_data.csv')

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

# Fill or drop missing values
df = df.fillna('N/A') 

# Handle ProductName Inconsistencies
print("\nStandardizing ProductName Column:")
df['ProductName'] = df['ProductName'].str.strip()    # Strip whitespaces from 'ProductName'
df['ProductName'] = df['ProductName'].str.lower()    # Convert 'ProductName' to lowercase

# Handle YearAdded Inconsistencies 
print("\nStandardizing YearAdded Format:")
df['YearAdded'] = pd.to_datetime(df['YearAdded'], errors='coerce').dt.year  

# Remove Duplicates - ProductName and ProductID
print("\nDuplicate Rows Check:")
print(df.duplicated().sum())  

# Remove duplicates based on 'ProductName' and 'ProductID' columns 
df = df.drop_duplicates(subset=['ProductName'], keep='first')
df = df.drop_duplicates(subset=['ProductID'], keep='first')

# Ensure non-negative UnitPrice 
print("\nChecking UnitPrice for Outliers:")
df['UnitPrice'] = df['UnitPrice'].apply(lambda x: x if x >= 0 else 0)  

# Filter UnitPrice outliers
Q1 = df['UnitPrice'].quantile(0.25)
Q3 = df['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['UnitPrice'] >= lower_bound) & (df['UnitPrice'] <= upper_bound)]


# Standardize Supplier Column
print("\nStandardizing Supplier Column:")
df['Supplier'] = df['Supplier'].str.strip().str.lower()  

# Final Quality Checks
print("\nFinal Quality Check:")
df.info() 
print("\nCleaned Data Head:")
print(df.head()) 

# Save cleaned data
df.to_csv('data/prepared/products_data_prepared.csv', index=False)

print("Data cleaned and saved to 'data/prepared/products_data_prepared.csv'")
