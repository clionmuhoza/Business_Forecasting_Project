import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
csv_file_path_vitamin = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/CA_NY_Vitamin_dataset.csv'
df_vitamin = pd.read_csv(csv_file_path_vitamin)

# Clean and standardize the 'Q-demos-age' column
df_vitamin['Age Group'] = df_vitamin['Q-demos-age'].str.strip()

# Define shared accounts: clean 'Q-amazon-use-howmany'
def check_shared_accounts(x):
    return x != '1 (just me!)' and pd.notna(x)  # True if account shared (anything other than '1 (just me!)')

df_vitamin['Shares Account'] = df_vitamin['Q-amazon-use-howmany'].apply(check_shared_accounts)

# Step 1: Count shared accounts per age group
shared_account_count = df_vitamin.groupby('Age Group')['Shares Account'].sum()

# Step 2: Top 3 sold vitamins per age group
top_vitamins = (
    df_vitamin.groupby('Age Group')['Vitamins Found']
    .apply(lambda x: x.value_counts().head(3))
)

# Filter out zero counts and rows where vitamin name is '0'
shared_account_count = shared_account_count[shared_account_count > 0]
top_vitamins = top_vitamins[top_vitamins.index.get_level_values(1) != '0']

# Output Results
print("Shared Account Counts by Age Group:")
print(shared_account_count)

print("\nTop 3 Sold Vitamins by Age Group:")
print(top_vitamins)

print("\nRun finished.")

# Plot shared account counts by age group
shared_account_count.plot(kind='bar', color='skyblue')
plt.title('Shared Account Counts by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Shared Accounts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
