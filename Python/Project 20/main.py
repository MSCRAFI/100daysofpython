from tkinter import *
import customtkinter
from customtkinter import *
customtkinter.set_appearance_mode("dark")
# GUI in class
class GUI(CTk):
    # function for GUI
    def __init__(self):
        super().__init__()
        self.geometry("600x400+400+150")  # starting GUI size
        self.title("Amar Notes")  # GUI title
        
        self.wm_iconbitmap("AmarNotesIcon.ico")  # GUI icon

#########################################################################
        
    # function for Menu    
    def amarMenu(self):
        mainMenu = Menu(self)  # Main menu
        self.config(menu=mainMenu)

        # Menu under main menu
        fileMenu = Menu(mainMenu, tearoff=0, bg="black", fg="white")
        mainMenu.add_cascade(label="File", menu=fileMenu)
        editMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="Edit", menu=editMenu)
        formatMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="Format", menu=formatMenu)
        viewMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="View", menu=viewMenu)
        helpMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="Help", menu=helpMenu)

#########################################################################

        # Functions for Filemenu command
        def newDef(self):
            pass

        def new_winDef():
            pass
        
        def openDef():
            pass
        
        def saveDef():
            pass
        
        def save_asDef():
            pass
        
        def page_setDef():
            pass
        
        def printDef():
            pass
        
        def exitDef():
            pass

        # Sub menu under File menu
        newMenu = Menu(fileMenu)
        fileMenu.add_command(label="New", command=newDef)

        new_winMenu = Menu(fileMenu)
        fileMenu.add_command(label="New Window", command=new_winDef)

        openMenu = Menu(fileMenu)
        fileMenu.add_command(label="Open...", command=openDef)

        saveMenu = Menu(fileMenu)
        fileMenu.add_command(label="Save", command=saveDef)

        save_asMenu = Menu(fileMenu)
        fileMenu.add_command(label="Save As...", command=save_asDef)

        fileMenu.add_separator()  # adding separator

        page_setMenu = Menu(fileMenu)
        fileMenu.add_command(label="Page Setup...", command=page_setDef)

        printMenu = Menu(fileMenu)
        fileMenu.add_command(label="Print...", command=printDef)

        fileMenu.add_separator()  # adding separator

        exitMenu = Menu(fileMenu)
        fileMenu.add_command(label="Exit", command=exitDef)

#########################################################################

    def notepad_Area(self):
        scrollbar = Scrollbar (self)  # Scrollbar for the notepad
        scrollbar.pack(side=RIGHT, fill=Y)

        notepad = Text(self, yscrollcommand=scrollbar.set, bg="#242424", fg="white", border=0, font="arial,sans-serif 11", insertbackground="white")  # Notepad text area
        notepad.pack(fill=BOTH)

#########################################################################

if __name__ == '__main__':
    window = GUI()
    window.amarMenu()
    window.notepad_Area()

    window.mainloop()
