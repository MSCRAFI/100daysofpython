# Exploring csv module
import csv
names = [["Salman", "Chowdhury"], ["ASM", "Hasan"]]
with open("name.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(names)
csvfile.close()
with open("name.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        print(i)
