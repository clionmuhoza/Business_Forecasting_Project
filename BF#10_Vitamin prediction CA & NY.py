import pandas as pd
import matplotlib.pyplot as plt

# Load the flu dataset
flu_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/CA_NY_flu_dataset.csv'
flu_df = pd.read_csv(flu_csv_file_path)

# Load the vitamin dataset
vitamin_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/CA_NY_Vitamin_dataset.csv'
vitamin_df = pd.read_csv(vitamin_csv_file_path)

# Filter for California and New York
states = ['California', 'New York']
vitamin_df['Shipping Address State'] = vitamin_df['Shipping Address State'].replace({'CA': 'California', 'NY': 'New York'})

# Ensure 'Order Date' and 'WEEKEND' columns are datetime
vitamin_df['Order Date'] = pd.to_datetime(vitamin_df['Order Date'], errors='coerce')
flu_df['WEEKEND'] = pd.to_datetime(flu_df['WEEKEND'], errors='coerce')

# --- Process Flu Data ---
filtered_flu_df = flu_df[flu_df['STATENAME'].isin(states)].copy()
filtered_flu_df['ACTIVITY LEVEL'] = pd.to_numeric(filtered_flu_df['ACTIVITY LEVEL'].astype(str).str.extract(r'(\d+)')[0], errors='coerce')
flu_pivot = filtered_flu_df.pivot(index='WEEKEND', columns='STATENAME', values='ACTIVITY LEVEL')

# --- Process Vitamin D Data ---
filtered_vitamin_df = vitamin_df[vitamin_df['Shipping Address State'].isin(states)].copy()
filtered_vitamin_df = filtered_vitamin_df[filtered_vitamin_df['Vitamins Found'].str.contains('Vitamin D', case=False, na=False)]

# Aggregate counts of Vitamin D per day and state
aggregated_vitamin_df = (
    filtered_vitamin_df
    .groupby(['Order Date', 'Shipping Address State'])
    .size()
    .reset_index(name='Vitamin D Count')
)
vitamin_pivot = aggregated_vitamin_df.pivot(index='Order Date', columns='Shipping Address State', values='Vitamin D Count')
vitamin_pivot = vitamin_pivot.resample('D').sum().fillna(0)

# --- Merge Flu and Vitamin D Data ---
combined_df = pd.merge(flu_pivot, vitamin_pivot, left_index=True, right_index=True, how='outer', suffixes=('_flu', '_vitamin'))
combined_df = combined_df.fillna(0)

# Filter data up to June 2023
combined_df = combined_df[combined_df.index <= '2023-06-30']

fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot Vitamin D sales
ax1.set_xlabel('Date')
ax1.set_ylabel('Vitamin D Sales', color='tab:blue')
ax1.plot(combined_df.index, combined_df['California_vitamin'], label='California Vitamin D Sales', color='tab:blue')
ax1.plot(combined_df.index, combined_df['New York_vitamin'], label='New York Vitamin D Sales', color='tab:cyan')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.legend(loc='upper left')

# Create a second y-axis for the flu data
ax2 = ax1.twinx()
ax2.set_ylabel('Flu Activity Level', color='tab:red')
ax2.plot(combined_df.index, combined_df['California_flu'], label='California Flu Activity', color='tab:red', alpha=0.5)
ax2.plot(combined_df.index, combined_df['New York_flu'], label='New York Flu Activity', color='tab:orange', alpha=0.5)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.legend(loc='upper right')

fig.tight_layout()
plt.title('Vitamin D Sales and Flu Activity Levels in California and New York')
plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))

# Plot for California
ax1.set_title('California: Vitamin D Sales and Flu Activity Levels')
ax1.set_xlabel('Date')
ax1.set_ylabel('Vitamin D Sales', color='tab:blue')
ax1.plot(combined_df.index, combined_df['California_vitamin'], label='Vitamin D Sales', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax3 = ax1.twinx()
ax3.set_ylabel('Flu Activity Level', color='tab:red')
ax3.plot(combined_df.index, combined_df['California_flu'], label='Flu Activity', color='tab:red', alpha=0.5)
ax3.tick_params(axis='y', labelcolor='tab:red')

# Plot for New York
ax2.set_title('New York: Vitamin D Sales and Flu Activity Levels')
ax2.set_xlabel('Date')
ax2.set_ylabel('Vitamin D Sales', color='tab:blue')
ax2.plot(combined_df.index, combined_df['New York_vitamin'], label='Vitamin D Sales', color='tab:cyan')
ax2.tick_params(axis='y', labelcolor='tab:blue')

ax4 = ax2.twinx()
ax4.set_ylabel('Flu Activity Level', color='tab:red')
ax4.plot(combined_df.index, combined_df['New York_flu'], label='Flu Activity', color='tab:orange', alpha=0.5)
ax4.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.show()