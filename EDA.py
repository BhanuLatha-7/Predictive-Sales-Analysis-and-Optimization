import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load historical sales data from a CSV file
sales_data = pd.read_csv('historical_sales_data.csv')

# Display basic statistics of numerical columns
print(sales_data.describe())

# Visualize sales volume distribution using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(sales_data['sales_volume'], bins=20, kde=True)
plt.title('Distribution of Sales Volume')
plt.xlabel('Sales Volume')
plt.ylabel('Frequency')
plt.show()

# Visualize relationship between sales volume and time of sale using a time series plot
sales_data['time_of_sale'] = pd.to_datetime(sales_data['time_of_sale'])
plt.figure(figsize=(12, 6))
sns.lineplot(x='time_of_sale', y='sales_volume', data=sales_data)
plt.title('Time Series of Sales Volume')
plt.xlabel('Time')
plt.ylabel('Sales Volume')
plt.show()

# Visualize sales volume by product category using a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='product_category', y='sales_volume', data=sales_data)
plt.title('Sales Volume by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales Volume')
plt.xticks(rotation=45)
plt.show()

# Visualize correlation matrix between numerical variables
plt.figure(figsize=(10, 6))
sns.heatmap(sales_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
