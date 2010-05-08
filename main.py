from Tkinter import *
import os

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Convert", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        os.system("echo peter");

root = Tk()

app = App(root)

root.mainloop()

