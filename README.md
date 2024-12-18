# ECON8310-Semy-Project

Welcome! This is our space to share ideas, code, and creativity. Let’s support each other and work together to build something great!

## Team Members
- Mouzam
- Gilian
- Clion

## Layout of scripts created
_Script 1: Cleaning and Preparing Vitamins_
The following script completes the cleaning and preparation of the Vitamin dataset for analysis: removal of columns, filtering of rows according to the survey response IDs, and a join of survey and purchase datasets. The cleaned dataset is then written to a CSV for further processing.

_Script 2: Merging Data Sets & Survey Analysis_
This script combines the survey data and the vitamin purchase records on a common identifier. Subsequent cleaning involves the removal of superfluous columns and labelling of potential issues with demographic and survey-based columns. It writes the combined data out for downstream analyses.

_Script 3: Dataset Exploration_
This script explores the combined dataset for things like the distribution of the product titles, customer demographics. Important: it is sparse in data and needs further cleaning, such as the removal of non-US residents.
Script 4: Distributions
Focused on analyzing age and income distributions, this script identifies customer demographics that are most profitable and active on the platform. It visualizes data distributions, emphasizing the preferred customer age (25–54 years) and income groups ($75,000–$149,999). These insights will help the “client” with defining the proposed target customers and marketing strategies.

_Script 4.1: Distributions in California and New York_
This script analyzes demographic trends in vitamin sales for California and New York. It examines shared account usage and identifies the top two vitamins sold by age group, providing insights into customer behaviors and preferences.

_Script 5: Correlation Analysis_
The following script calculates a correlation matrix such that demographic and behavioral variables are matched against the product purchases, encoding categorical variables and handling missing data to, finally, visualize the correlations in a heat map highlighting eventual predictors of the vitamins sales.

_Script 6: Vitamin analysis and filtering_
The script identifies and categorizes vitamins from the product title into binary flags of specific vitamins. Then, it calculates counts and distributions of vitamins across products, filtering the dataset by key states, such as CA, TX, and NY. It provides insights such as most sold vitamins, popular states that sell these vitamins, hence refining regional sales strategy.

_Script 7: Flu and Vitamin Data Analysis_
This script analyzes flu activity levels and vitamin sales in selected U.S. states, including California, Texas, New York, and Florida. It employs rolling averages to smooth the data and identifies the top five vitamins sold. The script then visualizes trends over time and highlights correlations between flu activity and vitamin sales, which can be further analyzed.

_Script 8: Vitamin D Export_
This script filters the dataset to include only products containing Vitamin D. It uses product titles to identify relevant entries and exports a filtered dataset for Vitamin D sales. This script focuses on Vitamin D trends for targeted analysis.

_Script 9: Vitamin Data for California and New York_
This script filters the dataset to include only vitamin sales in California and New York. It uses product titles to identify vitamins and exports a dataset specific to these states. This script enables localized analysis of vitamin sales trends.

_Script 10: Vitamin Prediction for California and New York_
This script integrates flu activity data and Vitamin D sales in California and New York. It processes the data to align timelines, aggregates weekly sales, and visualizes correlations between flu levels and Vitamin D purchases. This script supports predictive analysis of sales based on flu trends.

_Script 11: Correlation Matrix for Flu and Vitamin Data_
This script calculates a correlation matrix between flu activity levels and individual vitamins sold weekly. It preprocesses both datasets, aggregates data by week, and visualizes correlations to identify potential relationships between flu levels and vitamin consumption.

