import pandas as pd
import os

# Set the path 
csv_file_path = os.path.join('C:', 'Projects', 'smart-store-beaderstadt', 'data', 'raw', 'sales_data.csv')

# Read the CSV file 
data = pd.read_csv(csv_file_path)

# Calculate the average, minimum, and maximum SaleAmount
avg_sales = data['SaleAmount'].mean()
min_sales = data['SaleAmount'].min()
max_sales = data['SaleAmount'].max()

# Print the results
print(f"Average Sales: {avg_sales}")
print(f"Minimum Sales: {min_sales}")
print(f"Maximum Sales: {max_sales}")
