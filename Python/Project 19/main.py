from tkinter import *
root = Tk()

# Width x height
root.geometry("600x500+400+100")
root.minsize(300, 200)
root.maxsize(3000, 2000)
root.iconbitmap("AmarNotesIcon.ico")
root.title("Amar Notes")


# getImage = PhotoImage(file="AmarNotesIcon.png")
# showImage = Label(root, image=getImage).grid(row=0)
# myButton = Button(text="Click me")
# myButton.grid(row=0)


myMenu = Menu(root)
m1 = Menu(myMenu, tearoff=0)
m2 = Menu(m1, tearoff=0)
m2.add_command(label="Menu 2")
root.config(menu=myMenu)
myMenu.add_cascade(label="File", menu=m1)
m1.add_cascade(label="Menu 1", menu=m2)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(root, yscrollcommand=Scrollbar().set)
# for _ in range(100):
#     listbox.insert(END, f"Item {_}")
# listbox.pack()

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()
