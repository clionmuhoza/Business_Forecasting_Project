import pandas as pd

csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Combined_dataset.csv'

df = pd.read_csv(csv_file_path)

# List of vitamins to search for
vitamins = [
    'Vitamin A', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K',
    'B1', 'B2', 'B3',
    'B6', 'B12',
    'B5', 'B7', 'B9', 'Multivitamin'
]

# Add a mapping for alternative names
vitamin_aliases = {
    'biotin': 'B7',
    'folate': 'B9',
    'pantothenic': 'B5',
    'B-12': 'B12',
    'B vitamin': 'B12'
}

# Create a function to check for vitamins and label
def check_vitamins(title):
    if isinstance(title, str):
        title_lower = title.lower()  # Convert title to lowercase for case-insensitive matching
    else:
        title_lower = ''
    
    found_vitamins = []
    for vit in vitamins:
        if vit.lower() in title_lower:
            found_vitamins.append(vit)
    
    for alias, actual in vitamin_aliases.items():
        if alias.lower() in title_lower:
            found_vitamins.append(actual)
    
    return ', '.join(found_vitamins) if found_vitamins else '0'

# Apply the function to the Title column
df['Vitamins Found'] = df['Title'].apply(check_vitamins)

# Create columns for each vitamin
for vit in vitamins:
    df[vit] = df['Vitamins Found'].apply(lambda x: 1 if vit in x else 0)

# Filter the DataFrame to only include rows for the states CA and NY
filtered_df = df[df['Shipping Address State'].isin(['CA', 'NY'])]

# Export the filtered DataFrame to a new CSV file
output_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/CA_NY_Vitamin_dataset.csv'
filtered_df.to_csv(output_csv_file_path, index=False)

print("\nFiltered DataFrame for CA and NY:")
print(filtered_df.head())

# Find out how many time Vitamin D is mentioned, this helps with verifying the plots you will make in the future
vitamin_d_count = filtered_df['Vitamin D'].sum()
print(f"Number of Vitamin D in the dataset: {vitamin_d_count}")

print("Run finished")
