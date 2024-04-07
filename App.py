import pandas as pd

# Load historical sales data from a CSV file
sales_data = pd.read_csv('historical_sales_data.csv')

# Display the first few rows of the DataFrame
print(sales_data.head())
