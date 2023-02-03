import os


# function for png rename process
def rename_png():
    for i in files:
        if i[-3:] != "png":  # filtering the file format
            continue
        frmt.append(i)
        list_index = int(frmt.index(i)) + 1
        os.rename(f"{path}/{i}", f"{path}/{list_index}.png")  # rename the file


path = "."  # this is the path of folders. add "." if it is same folder
files = os.listdir(f"{path}")  # files or folders of selected path on list
frmt = []  # adding selected formats files
print(files)
rename_png()  # calling the function
