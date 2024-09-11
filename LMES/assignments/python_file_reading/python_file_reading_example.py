from pathlib import Path


""" Reading file content as String """

file_path = r"C:\Users\DELL\Downloads\python_read_raw_content.txt"

# with open(file_path, 'r') as file:
#     file_content = file.read()
#
# print(file_content)


""" Reading file content line by line """
# with open(file_path, 'r') as file:
#     file_content = ''
#     line = file.readline()
#
#     while line:
#         file_content += line
#         line = file.readline()
#
# print(file_content)


""" Reading file using Path library """
file_path = Path(r"C:\Users\DELL\Downloads\python_read_raw_content.txt")

file_content = file_path.read_text()

print(file_content)
