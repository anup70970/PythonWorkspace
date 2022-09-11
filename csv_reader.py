import csv

data = open(r'C:\Users\shedg\.vscode\PythonWorkspace\csv_pythn.csv')
file = csv.reader(data)
print(file)