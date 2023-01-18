import os

if not os.path.exists("New Files"):
    os.mkdir("New Files")
for i in range(0, 100):
    os.mkdir(f"New Files/Day {i+1}")
