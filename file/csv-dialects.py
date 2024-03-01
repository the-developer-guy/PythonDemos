import csv

print(csv.list_dialects())

with open("excel.csv", "wt", encoding="utf-8") as file:
    writer = csv.writer(file, dialect="excel")
    writer.writerow(["apple", 59])
    writer.writerow(["banana", 39])
    writer.writerow(["papaya", 99])

with open("excel-tab.csv", "wt", encoding="utf-8") as file:
    writer = csv.writer(file, dialect="excel-tab")
    writer.writerow(["apple", 59])
    writer.writerow(["banana", 39])
    writer.writerow(["papaya", 99])

with open("unix.csv", "wt", encoding="utf-8") as file:
    writer = csv.writer(file, dialect="unix")
    writer.writerow(["apple", 59])
    writer.writerow(["banana", 39])
    writer.writerow(["papaya", 99])

with open("manual.csv", "wt", encoding="utf-8", newline="\n") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["apple", 59])
    writer.writerow(["banana", 39])
    writer.writerow(["papaya", 99])
