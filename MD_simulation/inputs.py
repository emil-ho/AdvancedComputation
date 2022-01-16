# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:58:53 2021

@author: Pedro
"""
import re
import tkinter 
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk

def return_values():
    file=open('read_values.txt',"r+")
    for linea in file:
        if "fcc" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("FCC =",numbers)
        if "rd" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("rd =",numbers)
        if "rt" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("rt =",numbers)
        if "sig" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("sigma =",numbers)
        if "eps" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("epsilon =",numbers)
        if "cop" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("cop =",numbers)
        if "col" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("col =",numbers)
        if "ns" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("ns =",numbers)
        if "rs" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("rs =",numbers)
        if "wh" in linea:
            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            print("wh =",numbers)

def write_values(fcc1,rd,rt,sig,eps,cop,col,ns,rs,wh):
      
    f=open('read_values.txt',"r+")
    f.seek(0)
    f.write("fcc=")
    f.write(str(fcc1))
    f.write("\n")
    f.write("rd=")
    f.write(str(rd))
    f.write("\n")
    f.write("rt=")
    f.write(str(rt))
    f.write("\n")
    f.write("sig=")
    f.write(str(sig))
    f.write("\n")
    f.write("eps=")
    f.write(str(eps))
    f.write("\n")
    f.write("cop=")
    f.write(str(cop))
    f.write("\n")
    f.write("col=")
    f.write(str(col))
    f.write("\n")
    f.write("ns=")
    f.write(str(ns))
    f.write("\n")
    f.write("rs=")
    f.write(str(rs))
    f.write("\n")
    f.write("wh=")
    f.write(str(wh))
    f.truncate()

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

     #   global FCC
     #   FCC=fcc.get()
      #  global RD
       # RD=reducedD.get()
#        global RT
 #       RT=reducedT.get()
  #      global SIG
   #     SIG=sigma.get()
    #    global EPS
      #   EPS=epsilon.get()
#        global COFDLJ
 #       COFDLJ=cutoffP.get()
  #      global COFDNL
   #     COFDNL=cutoffL.get()
    #    global NS
     #   NS=numbersteps.get()
      #  global RTS
#        RTS=reducedt.get()
 #       global WH
  #      WH=widthb.get()
        

        
        
        #if (fcc.get()) == "":
    #        FCC=default_values[0]
     #   if (reducedD.get()) == "":
      #      RD=default_values[1]
     #          
      #  if (reducedT.get()) == "": 
       #     RT=default_values[2]
#
       # if sigma.get() == "":
      #      SIG=default_values[3]

      #  if epsilon.get() == "":
      #      EPS=default_values[4]

      #  if cutoffP.get() == "":
      #      COFDLJ=default_values[5]

      #  if (cutoffL.get()) == "":
     #       COFDNL=default_values[6]

      #  if (numbersteps.get()) == "":
      #      NS=default_values[7]

      #  if (reducedt.get()) == "":
      #      RTS=default_values[8]

      #  if (widthb.get()) == "":
      #      WH=default_values[9]
          

            root2.destroy()
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
        

        fcc1=fcc.get()

        rd=reducedD.get()

        rt=reducedT.get()

        sig=sigma.get()

        eps=epsilon.get()

        cop=cutoffP.get()

        col=cutoffL.get()

        ns=numbersteps.get()

        rs=reducedt.get()

        wh=widthb.get()
        
        
        
        
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
            root1.destroy()
            
            
        if (fcc1) == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "FCC" in linea:
                    fcc1=linea[4:]
            f.close()
        if (rd) == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "RD" in linea:
                    rd=linea[3:]
            f.close()
        if (rt) == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "RT" in linea:
                    rt=linea[3:]
            f.close()
     
        if sig == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "SIG" in linea:
                    sig=linea[4:]
            f.close()

        if eps == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "EPS" in linea:
                    eps=linea[4:]
            f.close()

        if cop == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "COFDLJ" in linea:
                    cop=linea[7:]
            f.close()

        if col == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "COFDNL" in linea:
                    col=linea[7:]
            f.close()

        if ns == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "NS" in linea:
                    ns=linea[3:]
            f.close()

        if rs == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "RS" in linea:
                    rs=linea[3:]
            f.close()

        if wh == "":
            f = open("default_values.txt", "r+")
            for linea in f:
                if "WH" in linea:
                    wh=linea[3:]
            f.close()
        write_values(fcc1, rd, rt, sig, eps, cop, col, ns, rs, wh)

        

        
        
        

    #Default values and quit options

    def button_9():

        
        print('Using default values...')
        f = open("default_values.txt", "r+")
        for linea in f:
            if "FCC" in linea:

                fcc1=linea[4:]

                    
            if "RD" in linea:

                rd=linea[3:]

                    
            if "RT" in linea:

                rt=linea[3:]

                    
            if "SIG" in linea:

                sig=linea[4:]


            if "EPS" in linea:

                eps=linea[4:]

        
            if "COFDLJ" in linea:

                cop=linea[7:]

            
            if "COFDNL" in linea:

                col=linea[7:]

            
            if "NS" in linea:

                ns=linea[3:]


            if "RS" in linea:

                rs=linea[3:]


            if "WH" in linea:

                wh=linea[3:]
            
        write_values(fcc1,rd,rt,sig,eps,cop,col,ns,rs,wh)
        root1.destroy()
        
    def button_10():
        print("a")
        
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

    root.destroy()
    archivo=tkinter.filedialog.askopenfile(mode='r')
    for linea in archivo:
        if "NumberFCCUnits" in linea:
            fcc1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "ReducedDensity" in linea:
            rd = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "ReducedTemperature" in linea:
            rt = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "Sigma" in linea:
            sig = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "Epsilon" in linea:
            eps = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "CutoffPotential" in linea:
            cop = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            
        if "CutoffList" in linea:
            col = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "NumberOfSteps" in linea:
            ns = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "ReducedTimeStep" in linea:
            rs = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]

        if "WidthBinPairDistributionFunction" in linea:
            wh = [float(s) for s in re.findall(r'-?\d+\.?\d*', linea)]
            
    write_values(fcc1,rd,rt,sig,eps,cop,col,ns,rs,wh)
   
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
    mybutton4 = tkinter.Button(root, text="Change default values", padx=51,pady=20,command=defaultvalues)
    mybutton4.pack()
    mybutton3 = tkinter.Button(root, text="Quit", padx=70,pady=20,command=button_3)
    mybutton3.pack()


    root.mainloop()

def defaultvalues():
    root.destroy()  


    root1=tkinter.Tk()
    root1.title("CHANGE DEFAULT VALUES")
    
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
    


    
    #Epsilon
    
    epsilon=ttk.Entry(root1,width=10)
    epsilon.grid(row=4,column=1)
    reducedtgrid1= tkinter.Label(root1,text="Epsilon parameter of the L-J potential : ")
    reducedtgrid1.grid(row=4,column=0)
    reducedtgrid= tkinter.Label(root1,text='Kelvin (K)')
    reducedtgrid.grid(row=4,column=2)
    

    
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
    def enter():

        f = open("default_values.txt", "r+")
        for linea in f:
            if "FCC" in linea:
                if (fcc.get()) == "":
                    fcc1=linea[4:]
                else:
                    fcc1=fcc.get()
                    
            if "RD" in linea:
                if (reducedD.get()) == "":
                    rd=linea[3:]
                else:
                    rd=reducedD.get()
                    
            if "RT" in linea:
                if (reducedT.get()) == "":
                    rt=linea[3:]
                else:
                    rt=reducedT.get()
                    
            if "SIG" in linea:
                if sigma.get() == "":
                    sig=linea[4:]
                else:
                    sig=sigma.get()

            if "EPS" in linea:
                if epsilon.get() == "":
                    eps=linea[4:]
                else:
                    eps=epsilon.get()
        
            if "COFDLJ" in linea:
                if cutoffP.get() == "":
                    cop=linea[7:]
                else:
                    cop=cutoffP.get()
            
            if "COFDNL" in linea:
                if (cutoffL.get()) == "":
                    col=linea[7:]
                else:
                    col=cutoffL.get()
            
            if "NS" in linea:
                if (numbersteps.get()) == "":
                    ns=linea[3:]
                else:
                    ns=numbersteps.get()

            if "RS" in linea:
                if (reducedt.get()) == "":
                    rs=linea[3:]
                else:
                    rs=reducedt.get()

            if "WH" in linea:
                if (widthb.get()) == "":
                    wh=linea[3:]
                else:
                    wh=widthb.get()
        try:
            float(fcc1)
            float(rd)
            float(rt)
            float(sig)
            float(eps)
            float(cop)
            float(col)
            float(ns)
            float(rs)
            float(wh)
            f.seek(0)
            f.write("FCC=")
            f.write(fcc1)
            f.write("\n")
            f.write("RD=")
            f.write(rd)
            f.write("\n")
            f.write("RT=")
            f.write(rt)
            f.write("\n")
            f.write("SIG=")
            f.write(sig)
            f.write("\n")
            f.write("EPS=")
            f.write(eps)
            f.write("\n")
            f.write("COFDLJ=")
            f.write(cop)
            f.write("\n")
            f.write("COFDNL=")
            f.write(col)
            f.write("\n")
            f.write("NS=")
            f.write(ns)
            f.write("\n")
            f.write("RS=")
            f.write(rs)
            f.write("\n")
            f.write("WH=")
            f.write(wh)
            f.truncate()


            f.close()
            root1.destroy()
        except:
            error3()
        
        
    
    button2=ttk.Button(root1,text="Enter",command=enter)
    button2.grid(row=11,column=2)


        

    
    #Quit
    def close():
        root1.destroy()
    
    button_quit=ttk.Button(root1,text="Quit",command=close)
    button_quit.grid(row=11,column=0)
    
    root1.mainloop()
    
