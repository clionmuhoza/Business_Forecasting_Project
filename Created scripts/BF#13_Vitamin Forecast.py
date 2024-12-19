import pandas as pd
from pygam import GAM, s
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Combined_dataset.csv')

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

df = df[df['Order Date'].dt.year < 2023]

df['Week'] = df['Order Date'].dt.isocalendar().week
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.isocalendar().year


# Aggregate data for weekly sales
weekly_sales = df.groupby(['Year', 'Week'])['Quantity'].sum().reset_index()
weekly_sales['Date'] = pd.to_datetime(weekly_sales['Year'].astype(str) + '-W' + weekly_sales['Week'].astype(str) + '-1', format="%Y-W%W-%w")
weekly_sales['Smoothed Sales'] = weekly_sales['Quantity'].rolling(window=3, min_periods=1, center=True).mean()

# Define the GAM model for weekly sales
X_weekly = weekly_sales[['Year', 'Week']]
y_weekly = weekly_sales['Quantity']
gam_weekly = GAM(s(0) + s(1))

# Fit the model
gam_weekly.fit(X_weekly, y_weekly)

# Forecast future weekly sales
last_year = weekly_sales['Year'].max()
last_week = weekly_sales['Week'].max()

future_weeks = pd.date_range(start=weekly_sales['Date'].max() + pd.Timedelta(weeks=1), periods=10, freq='W-MON')
future_weeks_df = pd.DataFrame({'Date': future_weeks})
future_weeks_df['Year'] = future_weeks_df['Date'].dt.year
future_weeks_df['Week'] = future_weeks_df['Date'].dt.isocalendar().week
X_future_weekly = future_weeks_df[['Year', 'Week']]

# Predict future weekly sales
future_weekly_sales = gam_weekly.predict(X_future_weekly)
future_weeks_df['Predicted Sales'] = future_weekly_sales
future_weeks_df['Smoothed Predicted Sales'] = pd.Series(future_weekly_sales).rolling(window=3, min_periods=1).mean()

# Combine weekly historical and future data for plotting
combined_weekly_sales = pd.concat([weekly_sales[['Date', 'Smoothed Sales']].rename(columns={'Smoothed Sales': 'Sales'}),
                                   future_weeks_df[['Date', 'Smoothed Predicted Sales']].rename(columns={'Smoothed Predicted Sales': 'Sales'})])

# Plot weekly sales
plt.figure(figsize=(14, 6))
plt.plot(combined_weekly_sales['Date'], combined_weekly_sales['Sales'], label='Actual and Predicted Sales', color='orange', linewidth=2)
plt.axvline(x=weekly_sales['Date'].max(), color='red', linestyle='--', label='Prediction Start')
plt.xlabel('Date')
plt.ylabel('Sales Quantity')
plt.legend()
plt.title('Weekly Sales Forecast')
plt.grid(True)
plt.tight_layout()
plt.show()

# Aggregate data for monthly sales
monthly_sales = df.groupby(['Year', 'Month'])['Quantity'].sum().reset_index()
monthly_sales['Date'] = pd.to_datetime(monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str) + '-01', format="%Y-%m-%d")
monthly_sales['Smoothed Sales'] = monthly_sales['Quantity'].rolling(window=3, min_periods=1, center=True).mean()

# Define the GAM model for monthly sales
X_monthly = monthly_sales[['Year', 'Month']]
y_monthly = monthly_sales['Quantity']
gam_monthly = GAM(s(0) + s(1))

# Fit the model
gam_monthly.fit(X_monthly, y_monthly)

# Forecast future monthly sales
last_year_month = monthly_sales['Year'].max()
last_month = monthly_sales['Month'].max()

future_months = pd.date_range(start=monthly_sales['Date'].max() + pd.Timedelta(days=1), periods=12, freq='MS')
future_months_df = pd.DataFrame({'Date': future_months})
future_months_df['Year'] = future_months_df['Date'].dt.year
future_months_df['Month'] = future_months_df['Date'].dt.month
X_future_monthly = future_months_df[['Year', 'Month']]

# Predict future monthly sales
future_monthly_sales = gam_monthly.predict(X_future_monthly)
future_months_df['Predicted Sales'] = future_monthly_sales
future_months_df['Smoothed Predicted Sales'] = pd.Series(future_monthly_sales).rolling(window=3, min_periods=1).mean()

# Combine monthly historical and future data for plotting
combined_monthly_sales = pd.concat([monthly_sales[['Date', 'Smoothed Sales']].rename(columns={'Smoothed Sales': 'Sales'}),
                                    future_months_df[['Date', 'Smoothed Predicted Sales']].rename(columns={'Smoothed Predicted Sales': 'Sales'})])

# Plot monthly sales
plt.figure(figsize=(14, 6))
plt.plot(combined_monthly_sales['Date'], combined_monthly_sales['Sales'], label='Actual & Predicted Sales', color='orange', linewidth=2)
plt.axvline(x=monthly_sales['Date'].max(), color='red', linestyle='--', label='Prediction Start')
plt.xlabel('Date')
plt.ylabel('Sales Quantity')
plt.legend()
plt.title('Monthly Sales Forecast')
plt.grid(True)
plt.tight_layout()
plt.show()
