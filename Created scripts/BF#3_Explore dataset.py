import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# In this script we are going to explore the dataset further and find out which variables already give insights to us and which we need to find more information about.

# Load the CSV file into a DataFrame
csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Combined_dataset.csv'
df = pd.read_csv(csv_file_path)

# Find sales of products in the 'Title' column
title_counts = df['Title'].value_counts()
PROD_titles = title_counts.head(10)
print(PROD_titles)
# 142   NatureWise Vitamin D3 5000iu (125 mcg) 1 Year Supply for Healthy Muscle Function, and Immune Support, Non-GMO, Gluten Free in Cold-Pressed Olive Oil, Packaging Vary ( Mini Softgel), 360 Count    
# 100   Nature’s Bounty Biotin, Supports Healthy Hair, Skin and Nails, 10,000 mcg, Rapid Release Softgels, 120 Ct                                                                                          
# 79    Nature's Bounty Vitamin B12, Supports Energy Metabolism, Tablets, 1000mcg, 200 Ct                                                                                                                  
# 76    Nature's Bounty Hair, Skin & Nails Rapid Release Softgels, Argan-Infused Vitamin Supplement with Biotin and Hyaluronic Acid, Supports Hair, Skin, and Nail Health for Women, 150 Count             
# 64    Nature’s Bounty Super B Complex with Vitamin C & Folic Acid, Immune & Energy Support, 150 tablets                                                                                                  
# 63    Nature's Bounty Optimal Solutions Hair, Skin & Nails Extra Strength, 150 Softgels

# This does not give us really insight, we don't know how many vitamin x are sold and if the numbers are a lot compared to the amount of products on the market.

# Count the number of different titles, to investigate the amount of products on the market.
num_unique_titles = df['Title'].nunique()
print(f'There are {num_unique_titles} different titles.')
# There are 2571 different titles, something that is not clear here is the amount of specific vitamin.

'---'

# Check if there are 50 states
title_counts = df['Q-demos-state'].value_counts()
VAR_states = title_counts.head(51)
print(VAR_states)
# There are 51 states, this is incorrect, so we will need to clean the it.

# Count the number of different titles in the states column, this will gave us the 1 title that is different and will be removed at the end.
num_unique_titles = df['Q-demos-state'].nunique()
print(f'There are {num_unique_titles} different titles.')
# There are 51 different titles.

'---'

# Check how many people use a wheelchair to see the need to include this data in the analysis
title_counts = df['Q-personal-wheelchair'].value_counts()
VAR_Wheelchair = title_counts.head(3)
print(VAR_Wheelchair)

#Wheel chair counts
#No                   10494
#Yes                    403
#Prefer not to say       11

'---'

# Understand the different Secual orientations in the dataset
title_counts = df['Q-sexual-orientation'].value_counts()
VAR_sexual_orientation = title_counts.head(3)
print(VAR_sexual_orientation)
#heterosexual (straight)    8970
#LGBTQ+                     1802
#prefer not to say           136

'---'

# Check if people lost a job and moved place of residence
title_counts = df['Q-life-changes'].value_counts()
VAR_Life_change = title_counts.head(50)
print(VAR_Life_change)
#Moved place of residence                1393
#Lost a job                               588
#Lost a job ,Moved place of residence     241
#Become pregnant                          239
#Had a child                              154

# This column could probably left out as it is only 20% of the dataset that has experienced a life change and the change is a move of residence or loss of job. Nothing directly related to Vitamin.
# You could maybe connect pregnancy to the vitamin intake, but this is a stretch.

'---'
# so based on this information we can see that the most frequent titles only make up 142 of the 2571 titles and a total of 10909 datapoints. 
# This means that the data is very sparse and we need to be careful with the analysis. 
# We also wanted to see what the most frequent titles are in the 'Q-demos-state' column.
# In here we found a datapoint we should delete, 'I did not reside in the United States'

df = df[df['Q-demos-state'] != 'I did not reside in the United States']

# Verify the datapoint has been removed
title_counts = df['Q-demos-state'].value_counts()
print(title_counts.head(51))

# Save the cleaned DataFrame to a new CSV file
#cleaned_csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Cleaned_dataset.csv'
#df.to_csv(cleaned_csv_file_path, index=False)

print("Run finished")
