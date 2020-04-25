import os
from time import sleep

import tkinter as Tk
from tkinter import *
import tkinter.font as font

from lang_processor import nlp


class WCUI:
    # window = ""

    def __init__(self):
        self.window = Tk()
        self.window.title("Web Customizer")
        self.window.geometry('800x800')
        self.window.config(bg = "white")
        self.window.overrideredirect(False)
        self.window.geometry(f"+{abs(0)}+{abs(0)}")
        self.nlpObject = nlp()


    def makeChanges(self, changes):
        print(changes)
        if( len(changes) >= 3  and  not(changes == None) and  not(changes == "")):
            self.nlpObject.proccessInput(changes)

    def mainmenu(self):
        myFont = font.Font(size=15)

        Titlee = Label(self.window, text="Type changes need here ..." ,bg="white")
        Titlee['font'] = myFont
        Titlee.pack(side=TOP,pady=10)

        inputText = Text(self.window, height=30, width = 800)
        inputText['font'] = myFont
        inputText.pack(side = TOP)

        button = Button(self.window, text="Apply Changes", width = 500 ,bg="blue", fg="white",command = lambda: self.makeChanges(inputText.get("1.0","end-1c")))
        button['font'] = myFont
        button.pack(side = BOTTOM)
        self.window.mainloop()

    
if __name__ == "__main__":
    WCUI().mainmenu()
