import csv
with open("output-onlinetools.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        if len(i["1st_column"]) != 5:
            continue
        print(i["1st_column"])