import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the CSV file into a DataFrame
csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Combined_dataset.csv'
if not os.path.exists(csv_file_path):
    print(f"Error: File does not exist at {csv_file_path}")
    exit()

df = pd.read_csv(csv_file_path)

columns_to_use = [
    'Purchase Price Per Unit', 'Quantity', 'Shipping Address State',
    'Q-demos-age', 'Q-demos-hispanic', 'Q-demos-race', 'Q-demos-education',
    'Q-demos-income', 'Q-demos-gender', 'Q-sexual-orientation',
    'Q-amazon-use-howmany', 'Q-amazon-use-hh-size', 'Q-amazon-use-how-oft',
    'Q-substance-use-cigarettes', 'Q-substance-use-marijuana', 'Q-substance-use-alcohol',
    'Q-personal-diabetes', 'Q-personal-wheelchair'
]

try:
    print("Filtering columns...")
    filtered_df = df[columns_to_use]
    print("Filtering complete. Shape:", filtered_df.shape)
except KeyError as e:
    print("Error: Missing columns in dataset.")
    print("Available columns:", df.columns)
    raise e

print("Dropping missing values...")
filtered_df = filtered_df.dropna(subset=columns_to_use)
print("Dropped missing values. Shape:", filtered_df.shape)

print("Encoding non-numeric columns...")
encoded_df = pd.get_dummies(filtered_df, drop_first=True)
print("Encoding complete. Shape:", encoded_df.shape)

print("Calculating correlation matrix...")
correlation_matrix = encoded_df.corr()
print("Correlation matrix calculation complete.")

print("Plotting correlation matrix...")
plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=False, fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

output_csv_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Correlation_Matrix.csv'
print(f"Saving correlation matrix to {output_csv_path}...")
correlation_matrix.to_csv(output_csv_path)
print("Correlation matrix saved.")