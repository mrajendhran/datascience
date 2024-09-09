import pandas as pd

# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)

""" Reading source file """
csv_file_data = pd.read_csv("housing_duplicates.csv")

""" Dropping rows if any duplicates values present in the data """
print("Dropping rows if any duplicates values present in the data")
csv_file_data.drop_duplicates(inplace=True)
print(csv_file_data.head())

""" Dropping duplicates values by specific field match """
print("Dropping duplicates values by specific field match")
csv_file_data.drop_duplicates(subset=['population','households'], inplace=True)
print(csv_file_data.head())

""" Renaming columns """
print(" Following statement will rename columns")
csv_file_data.rename(columns={"longitude":"long", "ocean_proximity": "Ocean_Border"}, inplace=True)
print(csv_file_data.head())
