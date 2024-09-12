import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("flights.csv")

""" Visualizing Statistical Relationships """

# relationship plot default shows scatter plot
# sns.relplot(x='passengers', y='month', hue='year', data=dataset)

linedata = sns.load_dataset("tips")

# line plot
# sns.relplot(x='time', y='tip', data=linedata, kind='line')


""" Plotting with Categorical Data """

# sns.catplot(x='day', y='total_bill', hue='day', data=linedata)

# violin plot
# sns.catplot(x='day', y='total_bill', hue='day', kind='violin', data=linedata)

# boxen plot
# sns.catplot(x='day', y='total_bill', hue='day', kind='boxen', data=linedata)


""" Visualizing the distribution of a dataset - Univariate and Bivariate distribution """

random_data = np.random.normal(loc=5, size=100, scale=2)
# displot - Univariate distribution
# sns.displot(random_data)

# bivariate_data = pd.read_csv("medical_bivariate.csv")
# Bar
# bivariate_data.plot.bar(stacked=True)

# Area
# bivariate_data.plot.area()

# Multi-Plot
iris_data_a = sns.load_dataset("iris")
iris_data_b = sns.FacetGrid(iris_data_a, col='species')
iris_data_b.map(plt.hist, 'sepal_length')

plt.show()