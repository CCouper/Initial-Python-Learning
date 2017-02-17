from tkinter import *

class Window (Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0, y=0)
        menu=Menu(self.master)
        self.master.config(menu=menu)

#Creating a file button, with a exit command in it
        file = Menu(menu)
        #.add_command adds a command to the drop down menu
        file.add_command(label="Save")
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

#Create an Edit button on the top menu
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)
#Create an empty menu on the top menu
        emptymenu = Menu(menu)
        menu.add_cascade(label="emptymenu", menu=emptymenu)




    def client_exit(self):
        exit()



root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
