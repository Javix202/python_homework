import csv

with open("../csv/employees.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

names = [f"{row[0]} {row[1]}" for row in data[1:]]
print(names)

names_with_e = [name for name in names if "e" in name.lower()]
print(names_with_e)