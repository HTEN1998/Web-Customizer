import os
from time import sleep

import tkinter as Tk
from tkinter import *
import tkinter.font as font

from lang_processor import nlp


class WCUI:
    # window = ""

    Sc_height = 0
    Sc_width = 0

    def __init__(self):
        self.window = Tk()
        self.window.title("Web Customizer")
        self.window.geometry('800x800')
        self.window.config(bg = "white")
        self.window.overrideredirect(False)
        
        self.Sc_height= self.window.winfo_screenheight()//2
        self.Sc_width= self.window.winfo_screenwidth()//2

        self.window.geometry(f"{self.Sc_width}x{self.Sc_height}")
        print(self.Sc_height)
        self.nlpObject = nlp()


    def makeChanges(self, changes):
        print(changes)
        if( len(changes) >= 3  and  not(changes == None) and  not(changes == "")):
           self.nlpObject.proccessInput(changes)
           pass

    def clearEntry(self, inputText):
        self.inputText.delete(0.0, 23.0)

    def mainmenu(self):
        myFont = font.Font(size=15)

        self.inputText = Text(self.window, height=self.Sc_height, width = self.Sc_width, bg="black", fg="white", insertbackground='white')
        self.inputText['font'] = myFont
        self.inputText.insert(0.0, 'Type changes need here ...')
        self.inputText.bind("<Button-1>", self.clearEntry)
        self.inputText.place(relx=0, rely=0)

        button = Button(self.window, text="Apply Changes", width = 500 ,bg="blue", fg="white",command = lambda: self.makeChanges(inputText.get("1.0","end-1c")))
        button['font'] = myFont
        button.pack(side = BOTTOM)
        self.window.mainloop()

    
if __name__ == "__main__":
    WCUI().mainmenu()
