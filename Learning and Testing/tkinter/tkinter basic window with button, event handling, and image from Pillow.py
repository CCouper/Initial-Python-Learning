from tkinter import *

from PIL import Image, ImageTk

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
        edit.add_command(label="Show Image", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showTxt)
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("ProfilePic.jpg")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self, text="Hey there good looking!")
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
