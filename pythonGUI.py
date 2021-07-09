# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 05:26:47 2020

@author: ptitf
"""
from tkinter import *

class Window(Frame):

    root = Tk()
    app = Window(root)
    root.wm_title("Timato")
    root.geometry("320x200")
    root.mainloop()



    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create Add Tasks button, link it to clickAddTasksButton()
        AddTasksButton = Button(self, text="Add Tasks", command=self.clickAddTasksButton)

        # create Delete Tasks button, link it to clickDelTasksButton()
        DelTasksButton = Button(self, text="Delete Tasks", command=self.clickDelTasksButton)

        # create Edit Tasks button, link it to clickEditTasksButton()
        EditTasksButton = Button(self, text="Edit Tasks", command=self.clickEditTasksButton)

        # create View Tasks button, link it to clickViewTasksButton()
        ViewTasksButton = Button(self, text="View Tasks", command=self.clickViewTasksButton)
        
        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
       
        # button locations
        AddTasksButton.place(x=100,y=100)
        DelTasksButton.place(x=300,y=100)
        EditTasksButton.place(x=500,y=100)
        ViewTasksButton.place(x=200,y=300)
        exitButton.place(x=400, y=300)
           
    def clickAddTasksButton(self):
        # declare the window
        window = Tk()
        # set window title
        window.title("Python GUI App")
        # set window width and height
        window.configure(width=500, height=300)
        # set window background color
        window.configure(bg='lightgray')
        window.mainloop()
    def clickDelTasksButton(self):
        pass
    def clickEditTasksButton(self):
        pass
    def clickViewTasksButton(self):
        pass
    def clickExitButton(self):
        exit()
        
