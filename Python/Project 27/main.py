import csv
with open("name.csv", "w") as csvfile:
    fieldnames = ["first_name", "middle_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first_name": "Salman", "middle_name": "Chowdhury", "last_name": "Rafi"})
    for i in range(10):
        first_name = input("Enter your first name:\n>> ")
        middle_name = input("Enter your middle name:\n>> ")
        last_name = input("Enter your last name:\n>> ")
        writer.writerow({"first_name": f"{first_name}", "middle_name": f"{middle_name}", "last_name": f"{last_name}"})