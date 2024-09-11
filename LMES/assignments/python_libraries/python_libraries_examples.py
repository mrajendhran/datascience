import pandas as pd

""" Reading a file """

csv_data_files = pd.read_csv("housing.csv")
# print("printing housing.csv file content")
# print(csv_data_files)
# print("printing top 10 items from the file")
# print(csv_data_files.head(10))
# print("printing last 10 items from the file")
# print(csv_data_files.tail(10))

"""r indicates reading content as it is"""
# raw_data_content = r"C:\Users\DELL\Downloads\python_read_raw_content.txt"
# print("printing raw content")
# print(raw_data_content)

""" EDA - Explorative Data Analysis """
# print("Explore the details about the data like, count, mean, std, min, mix...")
# print(csv_data_files.describe())
# print("Explore the details about the data type info, non-null count, dtype")
# print(csv_data_files.info())
# print("Printing column names")
# print(csv_data_files.columns)
# print("Using slicing operator from 3th to 7th index")
# print(csv_data_files[3:8])
# print("Using locator returns specific indices row data")
# print(csv_data_files.loc[[1,3,5,8]])
# print("Using locator returns specific indices row data with specific columns")
# print(csv_data_files.loc[[1,3,5,8], "ocean_proximity"])
# print("filter data with conditional operator")
# print(csv_data_files.loc[csv_data_files["ocean_proximity"] == "NEAR BAY"].head(3))
