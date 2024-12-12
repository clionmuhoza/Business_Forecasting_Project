import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the CSV file into a DataFrame
csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Combined_dataset.csv'
df = pd.read_csv(csv_file_path)

#Count the occurrences of each age group
age_distribution = df['Q-demos-age'].value_counts().sort_index()

# Plot the age distribution
plt.figure(figsize=(8, 6))
age_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age Group')
plt.ylabel('Number of People')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'---'

# Print the distribution for reference
print("Age Distribution:")
print(age_distribution)

# Count the occurrences of each income group
income_distribution = df['Q-demos-income'].value_counts().sort_index()

# Define the correct order for the income groups
income_order = [
    'Less than $25,000',
    '$25,000 - $49,999',
    '$50,000 - $74,999',
    '$75,000 - $99,999',
    '$100,000 - $149,999',
    '$150,000 or more'
]

# Reindex the income distribution to match the desired order
income_distribution = income_distribution.reindex(income_order)

# Plot the income distribution
plt.figure(figsize=(8, 6))
income_distribution.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Income Distribution')
plt.xlabel('Income Range')
plt.ylabel('Number of People')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print the distribution for reference
print("Income Distribution:")
print(income_distribution)