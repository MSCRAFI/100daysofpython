

def append_list():
    write_list_txt = open("list.txt", "a")
    my_list = []
    get_list = input("Enter your to do task list:\n>> ")
    my_list.append(get_list)
    write_list_txt.writelines(f"{my_list}\n")
    if get_list == "":
        write_list_txt.close()
    else:
        append_list()


append_list()
