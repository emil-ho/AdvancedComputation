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

default_values=[1,]*10

def error_3():
    root3.destroy()
    
def error3():
    global root3
    root3=tkinter.Tk()
    root3.title("ERROR")
    errorgrid= tkinter.Label(root3,text='Error, invalid input.')
    errorgrid.grid(row=1,column=1)
    errorgrid4= tkinter.Label(root3,text='The parameter must be a number.')
    errorgrid4.grid(row=2,column=1)
    button_close=ttk.Button(root3,text="Close",command=error_3)
    button_close.grid(row=4,column=1)
    root3.mainloop()
def returns(FCC,RD,RT,SIG,EPS,COFDLJ,COFDNL,NS,RTS,WH):
    try:
        float(FCC)
        float(RD)
        float(RT)
        float(SIG)
        float(EPS)
        float(COFDLJ)
        float(COFDNL)
        float(NS)
        float(RTS)
        float(WH)
        print(FCC)
        print(RD)
        print(RT)
        print(SIG)
        print(EPS)
        print(COFDLJ)
        print(COFDNL)
        print(NS)
        print(RTS)
        print(WH)
        parameters=[FCC,RD,RT,SIG,EPS,COFDLJ,COFDNL,NS,RTS,WH]
        return (parameters)
    except:
        error3()
    

def button_1():
    
    ######################################################################
 
    #Sigma Buttons
 
    def button_5():
        global sigma1
        sigma1= 'nanometers'
        nseconds= tkinter.Label(root1,text='nanometers (nm)')
        nseconds.grid(row=3,column=2)

        
    
    def button_6():
        global sigma1
        sigma1='Armstrongs'
        armstrongs= tkinter.Label(root1,text=' Armstrongs (A) ')
        armstrongs.grid(row=3,column=2)

        
    #EpsilonButtons
    
    def button_7():
        
        global epsilon1
        epsilon1='Kelvin (K)'
        kelvin= tkinter.Label(root1,text='Kelvin (K)')
        kelvin.grid(row=4,column=2)

        
    def button_8():
        
        global epsilon1
        epsilon1='Celsius'
        celsius= tkinter.Label(root1,text='Celsius (C)')
        celsius.grid(row=4,column=2)
        
    #Error message
        
    def error_2():
        root2.destroy()
        
    def error_1():
        a=fcc.get()
        b=reducedD.get()
        c=reducedT.get()
        d=sigma.get()
        e=epsilon.get()
        f=cutoffP.get()
        g=cutoffL.get()
        h=numbersteps.get()
        j=reducedt.get()
        k=widthb.get()
        

        root2.destroy()
        if (fcc.get()) == "":
            a=default_values[0]
        if (reducedD.get()) == "":
            b=default_values[1]
               
        if (reducedT.get()) == "": 
            c=default_values[2]

        if sigma.get() == "":
            d=default_values[3]

        if epsilon.get() == "":
            e=default_values[4]

        if cutoffP.get() == "":
            f=default_values[5]

        if (cutoffL.get()) == "":
            g=default_values[6]

        if (numbersteps.get()) == "":
            h=default_values[7]

        if (reducedt.get()) == "":
            j=default_values[8]

        if (widthb.get()) == "":
            k=default_values[9]

        
        returns(a,b,c,d,e,f,g,h,j,k)
        root1.destroy()
        
    def error():
        global root2
        root2=tkinter.Tk()
        root2.title("ERROR")
        errorgrid= tkinter.Label(root2,text='Error, one or more parameteres are missing.')
        errorgrid.grid(row=1,column=2)
        errorgrid2= tkinter.Label(root2,text='Missing parameters will be filled with default values')
        errorgrid2.grid(row=2,column=2)
        errorgrid3= tkinter.Label(root2,text='¿Do you want to continue?')
        errorgrid3.grid(row=3,column=2)
        button_yes=ttk.Button(root2,text="Yes",command=error_1)
        button_yes.grid(row=4,column=1)
        button_no=ttk.Button(root2,text="No",command=error_2)
        button_no.grid(row=4,column=3)
    
    #Enter button
        
    
    def button_4():
        
        a=fcc.get()
        b=reducedD.get()
        c=reducedT.get()
        d=sigma.get()
        e=epsilon.get()
        f=cutoffP.get()
        g=cutoffL.get()
        h=numbersteps.get()
        j=reducedt.get()
        k=widthb.get()
        
        if (fcc.get()) == "":
            error()
        elif (reducedD.get()) == "":
            error()
        elif (reducedT.get()) == "": 
            error()
        elif sigma.get() == "":
            error()
        elif epsilon.get() == "":
            error()
        elif cutoffP.get() == "":
            error()
        elif (cutoffL.get()) == "":
            error()
        elif (numbersteps.get()) == "":
            error()
        elif (reducedt.get()) == "":
            error()
        elif (widthb.get()) == "":
            error()
        else:
            returns(a,b,c,d,e,f,g,h,j,k)
            root1.destroy()
        
        

    #Default values and quit options

    def button_9():

        
        print('Using default values...')
        returns(default_values[0],default_values[1],default_values[2],default_values[3],
               default_values[4],default_values[5],default_values[6],default_values[7],
               default_values[8],default_values[9])
        root1.destroy()
        
    def button_10():
        root1.destroy()
        
    ################################################################
        
    root.destroy()
    root1=tkinter.Tk()
    root1.title("CHOOSE YOUR PARAMETERS ")
                            #Variables
                            
                            #FCC
                            
    fcc=ttk.Entry(root1,width=10)
    fcc.grid(row=0,column=1)
    fccgrid= tkinter.Label(root1,text='Number of FCC unit cells in each direction: ')
    fccgrid.grid(row=0,column=0)
    fccgrid1= tkinter.Label(root1,text='Integral number')
    fccgrid1.grid(row=0,column=2)
    
     #Reduced Density
     
    reducedD=ttk.Entry(root1,width=10)
    reducedD.grid(row=1,column=1)
    reducedDgrid= tkinter.Label(root1,text="Reduced density (adimensional) : ")
    reducedDgrid.grid(row=1,column=0)
    reducedDgrid1= tkinter.Label(root1,text='Adimensional')
    reducedDgrid1.grid(row=1,column=2)
    
    #Reduced Temperature
    
    reducedT=ttk.Entry(root1,width=10)
    reducedT.grid(row=2,column=1)
    reducedtgrid1= tkinter.Label(root1,text="Reduced temperature (adimensional) : ")
    reducedtgrid1.grid(row=2,column=0)
    reducedtgrid= tkinter.Label(root1,text='Adimensional')
    reducedtgrid.grid(row=2,column=2)
    
    #Sigma
    
    sigma=ttk.Entry(root1,width=10)
    sigma.grid(row=3,column=1)
    reducedtgrid1= tkinter.Label(root1,text="Sigma parameter of the L-J potential : ")
    reducedtgrid1.grid(row=3,column=0)
    reducedtgrid= tkinter.Label(root1,text='nanometers (nm)')
    reducedtgrid.grid(row=3,column=2)
    
    button_5=ttk.Button(root1,text="nanometers (nm)",command=button_5)
    button_5.grid(row=3,column=3)
    button_6=ttk.Button(root1,text="Armostrongs (A)",command=button_6)
    button_6.grid(row=3,column=4)

    
    #Epsilon
    
    epsilon=ttk.Entry(root1,width=10)
    epsilon.grid(row=4,column=1)
    reducedtgrid1= tkinter.Label(root1,text="Epsilon parameter of the L-J potential : ")
    reducedtgrid1.grid(row=4,column=0)
    reducedtgrid= tkinter.Label(root1,text='Kelvin (K)')
    reducedtgrid.grid(row=4,column=2)
    
    button_7=ttk.Button(root1,text="Kelvin (K)",command=button_7)
    button_7.grid(row=4,column=3)
    button_8=ttk.Button(root1,text="Celsius (C)",command=button_8)
    button_8.grid(row=4,column=4)
    
    #CutoffPotential
    
    cutoffP=ttk.Entry(root1,width=10)
    cutoffP.grid(row=5,column=1)
    cutoffpgrid1= tkinter.Label(root1,text="Cut off distance for L-J potential : ")
    cutoffpgrid1.grid(row=5,column=0)
    cutoffpgrid= tkinter.Label(root1,text='units of sigma')
    cutoffpgrid.grid(row=5,column=2)
    
    #CutoffList
    
    cutoffL=ttk.Entry(root1,width=10)
    cutoffL.grid(row=6,column=1)
    cutofflgrid1= tkinter.Label(root1,text="Cut off distance to compute neighbour list : ")
    cutofflgrid1.grid(row=6,column=0)
    cutofflgrid= tkinter.Label(root1,text='units of sigma')
    cutofflgrid.grid(row=6,column=2)
    
    #Number of steps
    
    numbersteps=ttk.Entry(root1,width=10)
    numbersteps.grid(row=7,column=1)

    numbersgrid1= tkinter.Label(root1,text= "Number of steps of the simulation : ")
    numbersgrid1.grid(row=7,column=0)
    numbersgrid= tkinter.Label(root1,text='Integral number')
    numbersgrid.grid(row=7,column=2)

    #Reduced time step
    
    reducedt=ttk.Entry(root1,width=10)
    reducedt.grid(row=8,column=1)

    reducedtgrid1= tkinter.Label(root1,text= "Reduced time step : ")
    reducedtgrid1.grid(row=8,column=0)
    reducedtgrid= tkinter.Label(root1,text='Adimensional')
    reducedtgrid.grid(row=8,column=2)

    #WidthBin
    
    widthb=ttk.Entry(root1,width=10)
    widthb.grid(row=9,column=1)
    widthbgrid1= tkinter.Label(root1,text= "Width of the Histogram bars: ")
    widthbgrid1.grid(row=9,column=0)
    widthbgrid= tkinter.Label(root1,text='Between 0 and 1')
    widthbgrid.grid(row=9,column=2)
    widthbgrid2= tkinter.Label(root1,text='')
    widthbgrid2.grid(row=10,column=0)
    widthbgrid3= tkinter.Label(root1,text='                                              ')
    widthbgrid3.grid(row=10,column=4)

    #BotOn enter
    
    button2=ttk.Button(root1,text="Enter",command=button_4)
    button2.grid(row=11,column=2)


    
    #Use default values
    
    button_default=ttk.Button(root1,text="Use default values",command=button_9)
    button_default.grid(row=11,column=4)
    
    #Quit
    
    button_quit=ttk.Button(root1,text="Quit",command=button_10)
    button_quit.grid(row=11,column=0)
    
    root1.mainloop()

def button_2():


    tkinter.filedialog.askopenfile(mode='r')
    root.destroy()



    
def button_3():
    root.destroy()
    
def mainbutton():
    global root
    root=tkinter.Tk()
    root.title('SELECT AN OPTION')
    mybutton1 = tkinter.Button(root, text="Enter input parameters directly", padx=29,pady=30,command=button_1)
    mybutton1.pack()
    mybutton2 = tkinter.Button(root, text="Choose a text file with the parameters", padx=10,pady=30,command=button_2)
    mybutton2.pack()
    mybutton3 = tkinter.Button(root, text="Quit", padx=70,pady=20,command=button_3)
    mybutton3.pack()

    root.mainloop()


