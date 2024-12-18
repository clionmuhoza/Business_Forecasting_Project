import pandas as pd

# In this script we are going to load our Vitamin dataset and combine it with the survey data set. This will be done based on the 'Survey ResponseID'

# First load the two datasets
vitamin_purchases = pd.read_csv('/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/vitamin_purchases.csv')
survey = pd.read_csv('//Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/survey.csv')

# Filter based on the column name SurveyResponseID
survey_response_column = "Survey ResponseID" 

# Filter the survey dataset to include the rows with SurveyResponseID that matches the Survey and vitamin_purchases datasets.
filtered_survey = survey[survey[survey_response_column].isin(vitamin_purchases[survey_response_column])]

# After the extraction of the data we can combine the two datasets based on the SurveyResponseID.
combined_data = pd.merge(vitamin_purchases, filtered_survey, on=survey_response_column)

'-------------------'
# with the merge we can continue to clean the data set by removing the columns that are not needed for the analysis.
# based on project proposal we can remove the following columns:
# - 'Product Code'
# - 'Category'
# - 'Survey ResponseID'
# - 'Q-domestic state'

# The code lines below remove the specified columns from the DataFrame
columns_to_remove = ['ASIN/ISBN (Product Code)', 'Category', 'Survey ResponseID', 'Q-demos-state']
df.drop(columns=columns_to_remove, inplace=True)

# Remove additional specified columns from the DataFrame
additional_columns_to_remove = [
    'Q-life-changes', 'Q-sell-YOUR-data', 'Q-sell-consumer-data', 
    'Q-small-biz-use', 'Q-census-use', 'Q-research-society'
]
df.drop(columns=additional_columns_to_remove, inplace=True)

# Columns to consider removing in a later stadium after checking for correlation:
# - 'Q-substance-use-cigarettes'
# - 'Q-substance-use-marijuana'
# - 'Q-substance-use-alcohol'


# Save the combined data to a new CSV file
combined_data.to_csv("/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Combined_dataset.csv", index=False)

print("Run finished")