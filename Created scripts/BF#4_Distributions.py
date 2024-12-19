import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the CSV file into a DataFrame
csv_file_path = r'/Users/giliankoenders/Documents/#TU Delft/USA Omaha/Business Forecasting/Midterm_project/Combined_dataset.csv'
df = pd.read_csv(csv_file_path)

# Count the occurrences of each age group
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

# The age distribution gives us the insides in who the customer is and how you could reach them. 

#Conclusion age:
#For the age group we used a rather simple distribution plot and with the outcomes in the table we made the conclusion that:
#The biggest group on the platform is roughly distributed the same and people familiar with internet and in particularly online shopping HAVE BOUGTH more on the platform. HAVE BOUGHT is really important to understand because we matched our survey data based on ID number and did not make an exception to include the survey data ones. This is important to understand, because if we would not do that the distribution for the 25-44 years would be different. This group has bought more per person, so the distribution shows the age group and the amount purchased, this gives us the targeted customer age. 
#The other thing is that the age is not normally distributed and you would not expect such a peak between the 18-24 years old and the two categories after, but again this is because of the amount purchased. A reason why the 18-24 buys less, is that they live at parents places and don’t have the money to afford all those vitamins. 

#Conclusion is that preferred customer age range is from 25 to 54 years old.

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



#Conclusion income:
#With the income distribution you can investigate what people are spending averagely based on what they earn. A higher average purchase price can be good for a company as it increases the profit margin as a whole. With the income distribution being almost complete levelled, targeting the higher end of the market can be more profitable. 

#Income is not normally distributed
#Interesting income group is:
#$75.000  - $99.999
#$100.000 - $149.999

#Reason is average purchase/ product is higher. And with that also the profit margin.

'---'
print("Run finished")

