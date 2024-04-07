import pandas as pd

# Load historical sales data from a CSV file
sales_data = pd.read_csv('historical_sales_data.csv')

# Convert 'time of sale' column to datetime format
sales_data['time_of_sale'] = pd.to_datetime(sales_data['time_of_sale'])

# Sort the data by time of sale
sales_data.sort_values(by='time_of_sale', inplace=True)

# Create lagged variables for sales volume (e.g., lagged sales for the previous month)
sales_data['lagged_sales_volume'] = sales_data['sales_volume'].shift(1)  # Shift by one month

# Calculate rolling averages for sales volume (e.g., 3-month rolling average)
sales_data['rolling_avg_sales_volume'] = sales_data['sales_volume'].rolling(window=3).mean()  # 3-month rolling average

# Create interaction terms between different variables (e.g., interaction between sales volume and product category)
sales_data['sales_product_interaction'] = sales_data['sales_volume'] * sales_data['product_category']

# Display the updated DataFrame with engineered features
print(sales_data.head())
