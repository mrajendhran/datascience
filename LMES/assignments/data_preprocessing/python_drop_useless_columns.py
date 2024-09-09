import pandas as pd

""" Reading CSV file into a variable """
csv_file_data = pd.read_csv("housing_drop_columns.csv")

""" Creating a data frame """
df = pd.DataFrame(csv_file_data)
""" Printing top 5 rows """
print(df.head())

""" Dropping columns by label/column name  
We can pass list of items to drop columns from data frame eg: ['ocean_proximity', 'tile_preference']"""
df.drop(['tile_preference'], axis=1, inplace=True)
print(df.head())

""" Dropping columns by index """
# df.drop(df.columns[9], axis=1, inplace=True)
# print(df.head())

""" Dropping columns by index 
Here you are specifying all rows with the colon (:) as the first argument of .loc[]. 
The second argument selects all columns between the "top_speed" and "passenger_capacity" columns. 
Together, we can get rid of useless columns by mentioning the column range.
"""
# df.drop(df.loc[:, "households":"ocean_proximity"], axis=1, inplace=True)
# print(df.head())