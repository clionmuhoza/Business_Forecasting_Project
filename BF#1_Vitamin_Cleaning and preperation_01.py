import pandas as pd

# Load the CSV file
file_path = '/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/vitamin_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("Original DataFrame:")
print(df.head())

#category_counts = df['Category'].value_counts() 
print(category_counts.head(50))

category_counts = df['Category'].value_counts() 
print(category_counts.head(50))
#In the category count we want to know how many times our chosen category is mentioned in the data set, for the VITAMIN catogery we see that it is 10908 times.

#Cleaning the data set
# Filter for rows where Category is "Vitamin"

vitamin_df = df[df['Category'] == 'VITAMIN']


# Save the filtered DataFrame to a new CSV file
vitamin_df.to_csv('vitamin_data.csv', index=False)
output_file_path = '/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/vitamin_purchases.csv'
vitamin_df.to_csv(output_file_path, index=False)

#Checking up with the new data set shows us that it contain 10908 rows and 10 columns. This matches our expectations and is veryfied by the catergory count performed earlier.

