import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("StudentsPerformance.csv")
# print("Understanding the dataset to see top 5 rows")
# print(dataset.head())

# print("Lets check total counts of the dataset")
# print(dataset.shape)

# print("Lets check describe to see all data information")
# print(dataset.describe())

# print("Lets check columns specific details")
# print(dataset.columns)

# print("Check unique values count")
# print(dataset.nunique())

# print("Check specific column unique values count")
# print(dataset['parental level of education'].nunique())


""" Cleaning dataset """

# print("Check any null in dataset")
# print(dataset.isna().sum())

# print("Dropping unuseful columns")
# dataset.drop(['race/ethnicity', 'parental level of education'], axis=1, inplace=True)
# print(dataset)

print("Relationship analysis")
corelation = dataset.corr(numeric_only=True)

# To plot relationship between variables
# sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)

# To plot each variable information
sns.pairplot(dataset)

# To histogram plot for two variables
# sns.relplot(x='math score', y='reading score', hue='gender', data=dataset)

# Histogram plot
# sns.displot(dataset['math score'])

# Categorical plot
# sns.catplot(x='reading score', kind='box', data=dataset)

plt.show()