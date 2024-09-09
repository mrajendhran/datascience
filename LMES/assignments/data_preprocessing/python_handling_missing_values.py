import pandas as pd

# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)

""" Reading source file """
csv_file_data = pd.read_csv("housing_with_empty_cell.csv")

""" Finding any null that are present in the data. 
If yes then column must have boolean True value otherwise it holds boolean False value """
# print("Printing boolean value based on null value present in the data.")
# finding_any_null = csv_file_data.isnull()
# print(finding_any_null)

""" Fill with 1000 number value wherever null / empty data are present. """
print("Fill with 1000 number value wherever null / empty data are present.")
data_fill_na = csv_file_data.fillna(1000)
print(data_fill_na.head())

""" Following print statement will not change original variable reference as it doesn't use inplace=True param. """
# print(csv_file_data.head())

""" Following statements will replace in original variable reference as we are passing inplace=True param. """
# csv_file_data.fillna(3000, inplace=True)
# print(csv_file_data.head())

""" Following statements will applicable to only ocean_proximity column replaced by number 5000. """
# csv_file_data['ocean_proximity'].fillna(5000, inplace=True)
# print(csv_file_data.head())

""" Following statements will applicable to only ocean_proximity column replaced by number 5000. """
# print("Following statements will applicable to only ocean_proximity column replaced by number 5000.")
# csv_file_data.fillna({"median_house_value": 2000, "ocean_proximity": 3000}, inplace=True)
# print(csv_file_data.head())

""" Following statements will applicable to only ocean_proximity column replaced by mean() housing_median_age column """
# print("Following statements will applicable to only ocean_proximity column replaced by mean() housing_median_age column")
# csv_file_data.fillna({"ocean_proximity": csv_file_data["housing_median_age"].mean(), "total_rooms": 3000}, inplace=True)
# print(csv_file_data.head())

""" Following statements will print number of null values are presented in the each columns """
# print("Following statements will print number of null values are presented in the each columns")
# total_null_of_house_value_and_proximity = csv_file_data[["median_house_value"]].isnull().sum().sum()
# print(total_null_of_house_value_and_proximity)


# print("Print total null sum for all the columns.....")
# total_count_of_is_null = csv_file_data.isnull().sum().sum()
# print(total_count_of_is_null)

# axis = 0 means drop rows, optional param & default value is axis=0
# axis = 1 means drop columns

# how = "any" default, or how = "all"
csv_file_data.dropna(inplace=True)
# csv_file_data.dropna(how="any", inplace=True)
print(csv_file_data.head(5))
