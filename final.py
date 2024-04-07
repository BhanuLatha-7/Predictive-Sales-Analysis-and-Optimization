import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load historical sales data from a CSV file
sales_data = pd.read_csv('historical_sales_data.csv')

# Convert 'time of sale' column to datetime format
sales_data['time_of_sale'] = pd.to_datetime(sales_data['time_of_sale'])

# Sort the data by time of sale
sales_data.sort_values(by='time_of_sale', inplace=True)

# Create lagged variables for sales volume (e.g., lagged sales for the previous month)
sales_data['lagged_sales_volume'] = sales_data['sales_volume'].shift(1)  # Shift by one month

# Drop missing values resulting from creating lagged variables
sales_data.dropna(inplace=True)

# Split the data into training and testing sets
X = sales_data[['lagged_sales_volume']].values
y = sales_data['sales_volume'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize XGBoost regressor
xgb = XGBRegressor(objective='reg:squarederror')

# Train the model
xgb.fit(X_train, y_train)

# Make predictions
y_pred = xgb.predict(X_test)

# Calculate RMSE (Root Mean Squared Error)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error (RMSE):', rmse)
