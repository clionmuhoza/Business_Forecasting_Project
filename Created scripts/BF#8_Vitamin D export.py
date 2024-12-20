import pandas as pd

# Load the dataset
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

# Filter the DataFrame to only include rows with Vitamin D
vitamin_d_df = df[df['Vitamin D'] == 1]

# Export the filtered DataFrame to a new CSV file
output_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Vitamin_D_dataset.csv'
vitamin_d_df.to_csv(output_csv_file_path, index=False)

print("\nFiltered DataFrame with Vitamin D:")
print(vitamin_d_df.head())

# Find out what the size is of the Vitamin D dataset
print("\nSize of the Vitamin D dataset:")
print(vitamin_d_df.shape)

print("Run finished")
