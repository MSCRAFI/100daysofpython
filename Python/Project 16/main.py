import os

choice = input("Do you want to create a main folder? (Type y/n)\n>> ")
if choice == "y":
    get_mfolder_name = input("Name of main folder you want to create:\n>> ")
    os.mkdir(f"{get_mfolder_name}")
    path = "/"
else:
    get_mfolder_name = ""
    path = ""
get_folder_name = input("Name of sub folder you want to create:\n>> ")
get_range = int(input("How many folders do you want to create?\n>> "))
for i in range(get_range):
    os.mkdir(f"{get_mfolder_name}{path}{get_folder_name} {i+1}")
