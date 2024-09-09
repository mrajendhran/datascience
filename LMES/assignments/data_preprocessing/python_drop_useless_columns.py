import pandas as pd

""" Reading CSV file """
df = pd.read_csv("housing_drop_columns.csv")
print(df.head())