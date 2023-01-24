import random as rd

# Choice list using matrix
mtrx_swg_list = [[0, 1, 2],
                 [2, 0, 1],
                 [1, 2, 0]]
score = {"Player:": 0, "PC:": 0}  # Score
swg_list = ["Snake", "Water", "Gun"] # List to print
while True:
    # random number for PC choice
    pc_choice = rd.randint(0, 2)
    # getting users choice
    get_usr_value = int(input("Choose a value to continue this game:\n\
    1. Snake\n\
    2. Water\n\
    3. Gun\n\
    >> "))
    # minus 1 to match it with pc choice
    get_usr_choice = get_usr_value - 1
    # to know if users choice is valid
    if get_usr_choice not in mtrx_swg_list[0]:
        print("Invalid Choice. Please choose again.")
        continue
    # users choice in the matrix
    for i in range(3):
        for j in range(3):
            if mtrx_swg_list[i][j] == get_usr_choice:
                get_usr_choice = [i, j]
    # checking who won
    if get_usr_choice[0] == pc_choice:
        score["Player:"] = score["Player:"] + 1
        print(f"{swg_list[get_usr_value - 1]} VS {swg_list[pc_choice]}. You win!! Your Total Win:", score["Player:"], "PC Total Win:\
", score["PC:"])
    elif get_usr_choice[0] != pc_choice:
        score["PC:"] = score["PC:"] + 1
        print(f"{swg_list[get_usr_value - 1]} VS {swg_list[pc_choice]}. You lose!! Your Total Win:", score["Player:"], "PC Total Win:\
", score["PC:"])
