"""Load a basic Excel file and sum the first column."""

import openpyxl

path = input("Please provide the Excel file's name: ")

workbook = openpyxl.load_workbook(filename=path)
sheet = workbook["Sheet1"]

sum = 0
for cell in sheet["A:A"]:
    sum += cell.value

print(f"The sum of column A is {sum}")
