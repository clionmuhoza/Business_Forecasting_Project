import pandas as pd
# import numpy as np

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

# Show the updated DataFrame
print(df)

# Summarize counts for each vitamin
vitamin_counts = df[vitamins].sum()

print("\nCounts of Each Vitamin:")
print(vitamin_counts)

# Print the vitamins in a separate column
df['Vitamins List'] = df[vitamins].apply(lambda row: ', '.join([vit for vit in vitamins if row[vit] == 1]), axis=1)

# Calculate the number of rows with no vitamins
no_vitamins_count = df[df['Vitamins Found'] == '0'].shape[0]
print(f"\nNumber of rows with no vitamins: {no_vitamins_count}")

# Calculate the distribution of products with multiple vitamins
df['Vitamin Count'] = df[vitamins].sum(axis=1)
vitamin_distribution = df['Vitamin Count'].value_counts().sort_index()
print("\nDistribution of products with multiple vitamins:")
print(vitamin_distribution)

# Export the updated DataFrame to a new CSV file
output_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Updated_Combined_dataset.csv'
df.to_csv(output_csv_file_path, index=False)

print("\nUpdated DataFrame with Vitamins List:")
print(df[['Title', 'Vitamins List']].head())
# Find the most common titles for rows with no vitamins
no_vitamins_titles = df[df['Vitamins Found'] == '0']['Title']
most_common_titles = no_vitamins_titles.value_counts().head(15)

print("\nMost Common Titles for Rows with No Vitamins:")
print(most_common_titles)

#Counts of Each Vitamin:
#Vitamin A     661
#Vitamin C    2325
#Vitamin D    2827
#Vitamin E     507
#Vitamin K     472
#Vitamin B1   2182
#Vitamin B2    235
#Vitamin B3    177
#Vitamin B6    485
#Vitamin B12  2152
#Vitamin B5    116
#Vitamin B7   1275
#Vitamin B9    828
#Multivitamin 2630


# Total dataset containts 10908 rows and the Vitamin selection has a total of 8658 rows. This means that 2250 rows do not contain any of the selected vitamins, 
# this is something we already predicted before we started the analysis because we could see that some are not directly related to vitamins.
# focus on the top 5 vitamins, Vitamin C, Vitamin D, Vitamin B1, Vitamin B12, and Vitamin E. These are the most common vitamins in the dataset and are likely to be the most relevant to the analysis.


# Filter the dataset for the specified states
states = ['CA', 'TX', 'NY', 'FL']

# Assuming the shipping address is in a column named 'Shipping Address'
df_filtered = df[df['Shipping Address State'].str.contains('|'.join(states), na=False)]

# Show the filtered DataFrame
print("\nFiltered DataFrame for specified states:")
print(df_filtered)

# Summarize counts for each vitamin in the filtered DataFrame
vitamin_counts_filtered = df_filtered[vitamins].sum()

print("\nCounts of Each Vitamin in Filtered DataFrame:")
print(vitamin_counts_filtered)

# Calculate the number of rows with no vitamins in the filtered DataFrame
no_vitamins_count_filtered = df_filtered[df_filtered['Vitamins Found'] == '0'].shape[0]
print(f"\nNumber of rows with no vitamins in filtered DataFrame: {no_vitamins_count_filtered}")

# Calculate the distribution of products with multiple vitamins in the filtered DataFrame
df_filtered['Vitamin Count'] = df_filtered[vitamins].sum(axis=1)
vitamin_distribution_filtered = df_filtered['Vitamin Count'].value_counts().sort_index()
print("\nDistribution of products with multiple vitamins in filtered DataFrame:")
print(vitamin_distribution_filtered)

# Export the filtered DataFrame to a new CSV file
output_csv_file_path_filtered = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Filtered_Combined_dataset.csv'
df_filtered.to_csv(output_csv_file_path_filtered, index=False)

print("\nFiltered DataFrame with Vitamins List:")
print(df_filtered[['Title', 'Vitamins List']].head())

# Find the most common titles for rows with no vitamins in the filtered DataFrame
no_vitamins_titles_filtered = df_filtered[df_filtered['Vitamins Found'] == '0']['Title']
most_common_titles_filtered = no_vitamins_titles_filtered.value_counts().head(15)

print("\nMost Common Titles for Rows with No Vitamins in Filtered DataFrame:")
print(most_common_titles_filtered)


#Counts of Each Vitamin in Filtered DataFrame:
#Vitamin A       209
#Vitamin C       680
#Vitamin D       844
#Vitamin E       134
#Vitamin K       139
#B1              710
#B2               57
#B3               52
#B6              139
#B12             700
#B5               38
#B7              379
#B9              211
#Multivitamin    767


print("Run finished")
