import pandas as pd

# Load raw data
df = pd.read_csv('data/raw/customers_data.csv')

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

# Handle Name Inconsistencies
print("\nStandardizing Name Column:")
df['Name'] = df['Name'].str.strip()    # Strip whitespaces from 'Name'
df['Name'] = df['Name'].str.lower()    # Convert 'Name' to lowercase 
df['Name'] = df['Name'].replace('hermione grager', 'hermione granger')  # Fix name typo

# Handle Date Inconsistencies
print("\nStandardizing JoinDate Format:")
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')  # Convert 'JoinDate' to datetime

# Remove Duplicates - Name and CustomerID
print("\nDuplicate Rows Check:")
print(df.duplicated().sum())  

# Remove duplicates based on 'Name' and 'CustomerID' columns 
df = df.drop_duplicates(subset=['Name'], keep='first')
df = df.drop_duplicates(subset=['CustomerID'], keep='first')

# Ensure non-negative LoyaltyPoints
print("\nChecking LoyaltyPoints for Outliers:")
df['LoyaltyPoints'] = df['LoyaltyPoints'].apply(lambda x: x if x >= 0 else 0)  

# Standardize PreferredContactMethod
print("\nStandardizing PreferredContactMethod Column:")
df['PreferredContactMethod'] = df['PreferredContactMethod'].str.lower()  # Convert 'PreferredContactMethod' to lowercase 

# Final Quality Checks
print("\nFinal Quality Check:")
df.info() 
print("\nCleaned Data Head:")
print(df.head()) 

# Save cleaned data
df.to_csv('data/prepared/customers_data_prepared.csv', index=False)

print("Data cleaned and saved to 'data/prepared/customers_data_prepared.csv'")
