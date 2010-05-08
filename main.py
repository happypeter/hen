from Tkinter import *
import os

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Convert", command=self.convert)
        self.hi_there.pack(side=LEFT)

    def convert(self):
        testInputFile = "/home/vivion/Desktop/music/steve/video/2"
        os.system("/home/vivion/convertor/convert.sh "+testInputFile)

root = Tk()

app = App(root)

root.mainloop()

