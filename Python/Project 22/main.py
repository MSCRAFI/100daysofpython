import os
import random as rd
import string


os.mkdir("Files")
for i in range(100):
    rd_alph = "".join(rd.choice(string.ascii_letters) for _ in range(6))
    open(f"Files\{rd_alph}{i}.txt", "w")