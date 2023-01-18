files = open("File.txt", "w")
lines = ["Hello\n", "My name is A.\n", "What is your name?\n"]
files.writelines(lines)
files.close()
