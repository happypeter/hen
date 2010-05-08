from Tkinter import *
import tkFileDialog
import os

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Convert", command=self.convert)
        self.hi_there.pack(side=LEFT)
        
        
        self.openFile = Button(frame, text="Open", command=open_it)
        self.openFile.pack(side=LEFT)

    def convert(self):
        os.system("/home/vivion/convertor/convert.sh "+filename)

def open_it():
    global filename 
    filename = tkFileDialog.askopenfilename()
    print filename

root = Tk()

app = App(root)

root.mainloop()

