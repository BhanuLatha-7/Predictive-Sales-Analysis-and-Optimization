import pandas as pd

# Load historical sales data from a CSV file
sales_data = pd.read_csv('historical_sales_data.csv')

# Handle missing values
sales_data.dropna(inplace=True)  # Drop rows with missing values

# Remove duplicates
sales_data.drop_duplicates(inplace=True)  # Remove duplicate rows

# Convert 'time of sale' column to datetime format
sales_data['time_of_sale'] = pd.to_datetime(sales_data['time_of_sale'])

# Aggregate the data to the appropriate level (e.g., monthly)
sales_data['month'] = sales_data['time_of_sale'].dt.to_period('M')  # Extract month from date
monthly_sales_data = sales_data.groupby('month').agg({
    'sales_volume': 'sum',
    'product_category': 'first',  # Assuming the product category remains constant within each month
    # Aggregate other relevant columns as needed
}).reset_index()

# Display the aggregated monthly sales data
print(monthly_sales_data.head())
