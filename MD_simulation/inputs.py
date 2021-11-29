# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:58:53 2021

@author: Pedro
"""

import tkinter 
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk

root=tkinter.Tk()


def button_1():
    def button_2():
        print(sigma.get())
        print(b.get())
        print(c.get())
        root1.destroy()
    root.destroy()
    root1=tkinter.Tk()
    sigma=ttk.Entry(root1,width=50)
    sigma.pack()
    sigma.insert(0,"Sigma: ")
    b=ttk.Entry(root1,width=50)
    b.pack()
    b.insert(0, "Lambda: ")
    c=ttk.Entry(root1,width=50)
    c.pack()
    button2=ttk.Button(root1,text="Enter",command=button_2)
    button2.pack()
    c.insert(0, "delta t: ")

    root1.mainloop()

def button_2():

    root.destroy()
    root2=tkinter.Tk()
    tkinter.filedialog.askopenfile(mode='r')
    root2.mainloop()


    
def button_3():
    root.destroy()
mybutton1 = tkinter.Button(root, text="Input parameters", padx=35,pady=35,command=button_1)
mybutton1.pack()
mybutton2 = tkinter.Button(root, text="Text file", padx=60,pady=40,command=button_2)
mybutton2.pack()
mybutton3 = tkinter.Button(root, text="Quit", padx=70,pady=20,command=button_3)
mybutton3.pack()

root.mainloop()

