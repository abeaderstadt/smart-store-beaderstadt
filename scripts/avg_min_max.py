import pandas as pd


data = pd.read_csv('sales_data.csv')

# Calculate the average, minimum, and maximum SaleAmount
avg_sales = data['SaleAmount'].mean()
min_sales = data['SaleAmount'].min()
max_sales = data['SaleAmount'].max()

# Print the results
print(f"Average Sales: {avg_sales}")
print(f"Minimum Sales: {min_sales}")
print(f"Maximum Sales: {max_sales}")
