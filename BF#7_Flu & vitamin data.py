import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Updated_Combined_dataset.csv'
df = pd.read_csv(csv_file_path)

# Load the flu dataset
flu_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/StateDatabySeasonflu.csv'
flu_df = pd.read_csv(flu_csv_file_path)

# Filter the flu dataset for the specified states
states = [
    'California', 'Texas', 'New York', 'Florida'
]

filtered_flu_df = flu_df[flu_df['STATENAME'].isin(states)].copy()

# Change 'WEEKEND' column t0 datetime
if 'WEEKEND' in filtered_flu_df.columns:
    filtered_flu_df.loc[:, 'WEEKEND'] = pd.to_datetime(filtered_flu_df['WEEKEND'], format='%b-%d-%Y')
    filtered_flu_df = filtered_flu_df.sort_values(by='WEEKEND')  # Ensure sorted by time

# Convert 'ACTIVITY LEVEL' to numeric, forcing errors to NaN
filtered_flu_df['ACTIVITY LEVEL'] = pd.to_numeric(filtered_flu_df['ACTIVITY LEVEL'].str.extract('(\d+)')[0], errors='coerce')

flu_pivot = filtered_flu_df.pivot(index='WEEKEND', columns='STATENAME', values='ACTIVITY LEVEL')

# Apply a rolling average for smoothing
rolling_window = 4  # Adjust for more/less smoothing
smoothed_flu = flu_pivot.rolling(window=rolling_window, min_periods=1).mean()

# Plot the smoothed flu activity levels for the specified states
plt.figure(figsize=(15, 10))

for state in states:
    if state in smoothed_flu.columns:
        plt.plot(smoothed_flu.index, smoothed_flu[state], label=state)

plt.title('Smoothed Flu Activity Levels Over Time', fontsize=16)
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Flu Activity Level', fontsize=12)
plt.legend(title="States", loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


# Defining the vitamin categories
vitamins = [
    'Vitamin A', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K',
    'B1', 'B2', 'B3',
    'B6', 'B12',
    'B5', 'B7', 'B9', 'Multivitamin'
]

# Ensure 'Order Date' column exists and is datetime
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df = df.sort_values(by='Order Date')  # Ensure sorted by time

# Calculate total products sold for each vitamin category per day
daily_sales = df.groupby('Order Date')[vitamins].sum()

# Apply a rolling average for smoothing
rolling_window = 35  # Adjust for more/less smoothing
smoothed_sales = daily_sales.rolling(window=rolling_window, min_periods=1).mean()

# Identify the top 5 vitamins with the highest total sales
total_sales = smoothed_sales.sum()
top_5_vitamins = total_sales.nlargest(5).index.tolist()

# Plot the smoothed sales trends for the top 5 vitamins
plt.figure(figsize=(15, 10))

for vitamin in top_5_vitamins:
    if vitamin in smoothed_sales.columns:
        plt.plot(smoothed_sales.index, smoothed_sales[vitamin], label=vitamin)

plt.title('Smoothed Top 5 Vitamin Sales Over Time', fontsize=16)
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.legend(title="Vitamins", loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# Filter the flu dataset for California and New York
ca_ny_flu_df = flu_df[flu_df['STATENAME'].isin(['California', 'New York'])].copy()

# Ensure 'WEEKEND' column exists and is datetime
if 'WEEKEND' in ca_ny_flu_df.columns:
    ca_ny_flu_df.loc[:, 'WEEKEND'] = pd.to_datetime(ca_ny_flu_df['WEEKEND'], format='%b-%d-%Y')
    ca_ny_flu_df = ca_ny_flu_df.sort_values(by='WEEKEND')  # Ensure sorted by time

# Convert 'ACTIVITY LEVEL' to numeric, forcing errors to NaN
ca_ny_flu_df['ACTIVITY LEVEL'] = pd.to_numeric(ca_ny_flu_df['ACTIVITY LEVEL'].str.extract('(\d+)')[0], errors='coerce')

# Save the filtered dataset to a new CSV file
#ca_ny_flu_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/CA_NY_flu_dataset.csv'
#ca_ny_flu_df.to_csv(ca_ny_flu_csv_file_path, index=False)

print("Run finished")
