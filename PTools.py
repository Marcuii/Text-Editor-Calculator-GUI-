import re
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import math
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter import Label, Tk 
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
 
#General GUI Code:
#----------------
root = Tk()
root.resizable(0, 0)
#----------------  


#Main Window:
#----------------
class MainWin( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("PTools") 
        self.configure(bg='#085c74')
        
        #Buttons Section:
        self.pnote = Button( self, text = "PNote", width = 110,
                             command = self.opennote)
        self.pnote.grid( row = 0, column = 0, sticky = N) 
        
        self.calc = Button( self, text = "PCalculator", width = 90,
                             command = self.opencalc)
        self.calc.grid( row = 1, column = 0, sticky = N)         
        
        self.about = Button( self, text = "About PTeam", width = 70,
                             command = self.aboutwin)
        self.about.grid( row = 2, column = 0, sticky = N) 
        
        self.end = Button( self, text = "Exit", width = 50,
                             command = self.end)
        self.end.grid( row = 3, column = 0, sticky = N)
        
    #Functions of Buttons:  
    def opennote(self):
        self.destroy()
        PNote()
        
    def opencalc(self):
        self.destroy()
        PCalc()
        
    def aboutwin(self):
        About()    
        
    def end(self):
        if messagebox.askyesno("PTools", "Are you sure you want to exit?"):
            root.destroy() 
#----------------


#PNote Window:
#----------------
class PNote( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("PNote")
        self.configure(bg='#085c74')
        
#Open Button:        
        self.open = Button( self, text = "Open", width = 110,
                             command = self.open) 
        self.open.grid( row = 0, column = 0, sticky = W) 
        
#Save Button:                
        self.save = Button( self, text = "Save", width = 75,
                             command = self.save)  
        self.save.grid( row = 0, column = 0, sticky = N)
        
#Font Control Button:                
        self.font = Button( self, text = "Font", width = 110)        
        self.font.grid( row = 0, column = 0, sticky = E)  
        
#Edit Menu for the text place:        
        self.editmenu = Menubutton ( self, text="Edit Menu", width = 107)
        self.editmenu.grid(row = 1, column = 0, sticky = W) 
        self.editmenu.menu =  Menu ( self.editmenu, tearoff = 0 )
        self.editmenu["menu"] = self.editmenu.menu 
    #Clear Button:
        self.editmenu.menu.add_command ( label="Clear",
                                  command=self.clear )
    #Cut Button:
        self.editmenu.menu.add_command ( label="Cut",
                                  command=self.cut ) 
    #Copy Button:
        self.editmenu.menu.add_command ( label="Copy",
                                  command=self.copy )
    #Paste Button:
        self.editmenu.menu.add_command ( label="Paste",
                                  command=self.paste )
    #SelectAll Button:
        self.editmenu.menu.add_command ( label="Select All",
                                  command=self.selectAll )
    #Separater:
        self.editmenu.menu.add_command (label="---------", state=DISABLED)
             

#About Button:
        self.about = Button( self, text = "About", width = 75,
                             command = self.aboutwin)        
        self.about.grid( row = 1, column = 0, sticky = N)  
        
#Exit Button:        
        self.back = Button( self, text = "Main Menu", width = 110,
                             command = self.exit)        
        self.back.grid( row = 1, column = 0, sticky = E) 
        
#Notepad Section (Typing place):        
        self.notepad = ScrolledText(self, width = 225, height = 40, bg= "#e8e4e4")        
        self.notepad.grid( row = 2, sticky = W+E+N+S )
        
#Date and Time section:  
        self.timelabel = Label(self, font =("Courier", 15),bg='#085c74')
        self.timelabel.grid( row = 3, column = 0, sticky = S)
        self.dateandtime()
        
                
#Functions and Commands:
    #Open File Command:
    def open(self):
        fd = filedialog.askopenfile(parent = root, mode = 'r')
        t = fd.read()
        self.notepad.delete(0.0, END)
        self.notepad.insert(0.0, t)
    
    #Save File Command:    
    def save(self):
        fd = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
        if fd!= None:
            data = self.notepad.get('1.0', END)
        try:
            fd.write(data)
        except:
            messagebox.showerror(title="Error", message = "Couldn't save your file!") 
            
    #Font Control:
    #######Couldn't Find it yet#######        
            
    #Clear Notepad Command:        
    def clear(self):
        self.notepad.delete(0.0, END) 
    
    #Cut Command:    
    def cut(self):
        self.notepad.event_generate("<<SelectAll>>")        
        self.notepad.event_generate("<<Cut>>")
    
    #Copy Command:
    def copy(self):
        self.notepad.event_generate("<<SelectAll>>")                
        self.notepad.event_generate("<<Copy>>")
    
    #Paste Command:
    def paste(self):
        self.notepad.event_generate("<<Paste>>")
    
    #SelcetAll Command:    
    def selectAll(self):     #edit menu Select All option
        self.notepad.event_generate("<<SelectAll>>")          
    
    #Date and Time label:   
    def dateandtime(self):
        current_dt = datetime.now()
        dt = current_dt.strftime("Date: %d/%m/%Y \nTime: %H:%M:%S")          
        self.timelabel.config(text=dt)
        self.timelabel.after(200, self.dateandtime)
        
    #To open about window:
    def aboutwin(self):
        About()
    
    #To back to main menu:
    def exit(self):     #file menu Exit option
        if messagebox.askyesno("PNote", "Are you sure you want to back to main menu?"):
            self.destroy()    
            MainWin()
#----------------


#PCalc Window:
#----------------
class PCalc( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("PCalculator")
        self.configure(bg='#085c74')
	
	#Variables for the operations:
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False	
        
        #Main Menu Button:
        self.back = Button( self, text = "Main Menu", width = 50, command = self.exit).grid( row = 0, column = 0, columnspan=4, sticky = N)     
        
        #Calculator Screen:        
        self.txtDisplay = Entry(self, font=('Helvetica',20,'bold'))
        self.txtDisplay.grid(row=1,column=0, columnspan=4, pady=1)
        self.txtDisplay.insert(0,"0")
	
	#Clear Button:
        self.btnClear = Button(self, text="Clear", width = 50, command=self.clear).grid(row=2, column= 0, columnspan=4, pady = 1)
	
	#Operations and Numbers:
        self.btnln = Button(self, text="ln", command=self.ln).grid(row=3, column= 0, pady = 1)
        
        self.btnlog = Button(self, text="log", command=self.log).grid(row=3, column= 1, pady = 1)	
        
        self.btne = Button(self, text="e", command=self.e).grid(row=3, column= 2, pady = 1)        
                
        self.btnroot = Button(self, text="\u221A", command=self.root).grid(row=3, column= 3, pady = 1)        
                
        self.btnsin = Button(self, text="Sin", command=self.sin).grid(row=4, column= 0, pady = 1)  
        
        self.btncos = Button(self, text="Cos", command=self.cos).grid(row=4, column= 1, pady = 1)
        
        self.btntan = Button(self, text="Tan", command=self.tan).grid(row=4, column= 2, pady = 1)
        	
        self.btnAdd = Button(self, text="+", command=lambda:self.operation("add")).grid(row=4, column= 3, pady = 1) 

        self.btn9 = Button(self, text="9", command=lambda:self.numberEnter(9)).grid(row=5, column= 0, pady = 1)
	
        self.btn8 = Button(self, text="8", command=lambda:self.numberEnter(8)).grid(row=5, column= 1, pady = 1)
	
        self.btn7 = Button(self, text="7", command=lambda:self.numberEnter(7)).grid(row=5, column= 2, pady = 1)
        
        self.btnsub = Button(self, text="-", command=lambda:self.operation("sub")).grid(row=5, column= 3, pady = 1) 
	
        self.btn6 = Button(self, text="6", command=lambda:self.numberEnter(6)).grid(row=6, column= 0, pady = 1)
	
        self.btn5 = Button(self, text="5", command=lambda:self.numberEnter(5)).grid(row=6, column= 1, pady = 1)
	
        self.btn4 = Button(self, text="4", command=lambda:self.numberEnter(4)).grid(row=6, column= 2, pady = 1)
	
        self.btndiv = Button(self, text="÷", command=lambda:self.operation("divide")).grid(row=6, column= 3, pady = 1) 	
	
        self.btn3 = Button(self, text="3", command=lambda:self.numberEnter(3)).grid(row=7, column= 0, pady = 1)
	
        self.btn2 = Button(self, text="2", command=lambda:self.numberEnter(2)).grid(row=7, column= 1, pady = 1)
	
        self.btn1 = Button(self, text="1", command=lambda:self.numberEnter(1)).grid(row=7, column= 2, pady = 1)
	
        self.btnmult = Button(self, text="x", command=lambda:self.operation("multi")).grid(row=7, column= 3, pady = 1) 	
	
        self.btn0 = Button(self, text="0", command=lambda:self.numberEnter(0)).grid(row=8, column= 0, pady = 1)
	
        self.btndot = Button(self, text=".", command=lambda:self.numberEnter(".")).grid(row=8, column= 1, pady = 1)
	
        self.btnpi = Button(self, text="π", command=self.pi).grid(row=8, column= 2, pady = 1)
	
        self.btnequal = Button(self, text="=", command=self.sum_of_total).grid(row=8, column= 3, pady = 1)	
	    
    #To back to main menu:
    def exit(self):     #file menu Exit option
        self.destroy()    
        MainWin() 
    
    #Screen Function:
    def display(self, value):
	    self.txtDisplay.delete(0, END)
	    self.txtDisplay.insert(0, value)    
    
    #Clear Button:
    def clear(self):
	    self.result = False
	    self.current = "0"
	    self.display(0)
	    self.input_value=True		
	    self.total=0  
    
    #Operations functions:
    def ln(self):
	    self.result = False
	    self.current = math.log(float(self.txtDisplay.get()))
	    self.display(self.current)

    def log(self):
	    self.result = False
	    self.current = math.log10(float(self.txtDisplay.get()))
	    self.display(self.current) 
    
    def e(self):
	    self.result = False
	    self.current = math.e
	    self.display(self.current)

    def root(self):
	    self.result = False
	    self.current = math.sqrt(float(self.txtDisplay.get()))
	    self.display(self.current)
    
    def sin(self):
	    self.result = False
	    self.current = math.sin(math.radians(float(self.txtDisplay.get())))
	    self.display(self.current)
    
    def cos(self):
	    self.result = False
	    self.current = math.cos(math.radians(float(self.txtDisplay.get())))
	    self.display(self.current)

    def tan(self):
	    self.result = False
	    self.current = math.tan(math.radians(float(self.txtDisplay.get())))
	    self.display(self.current)    

    def pi(self):
	    self.result = False
	    self.current = math.pi
	    self.display(self.current) 
    
    def numberEnter(self, num):
	    self.result=False
	    firstnum=self.txtDisplay.get()
	    secondnum=str(num)
	    if self.input_value:
		    self.current = secondnum
		    self.input_value=False
	    else:
		    if secondnum == '.':
			    if secondnum in firstnum:
				    return
		    self.current = firstnum+secondnum
	    self.display(self.current)    
    
    def operation(self, op):
	    self.current = float(self.current)
	    if self.check_sum:
		    self.valid_function()
	    elif not self.result:
		    self.total=self.current
		    self.input_value=True
	    self.check_sum=True
	    self.op=op
	    self.result=False
    
    def valid_function(self):
	    if self.op == "add":
		    self.total += self.current
	    if self.op == "sub":
		    self.total -= self.current
	    if self.op == "multi":
		    self.total *= self.current
	    if self.op == "divide":
		    self.total /= self.current
	    self.input_value=True
	    self.check_sum=False
	    self.display(self.total)
	    
    def sum_of_total(self):
	    self.result=True
	    self.current=float(self.current)
	    if self.check_sum==True:
		    self.valid_function()
	    else:
		    self.total=float(self.txtDisplay.get())        
#----------------


#About Window:   
#----------------
class About(Frame):     
    def __init__(self):
        about = tk.Frame.__init__(self)
        about = Toplevel(self)
        about.title("About")
        about.geometry("550x215")
        about.resizable(0, 0)
        about.configure(bg='#085c74')	
        
        #Labels Section:
        about.title = Label( about, text = "The PTools", bg='#085c74', font =("Courier", 50))
        about.create = Label( about, text = "Created by:",bg='#085c74')
        about.marc = Label( about, text = "1- Marcleino Emad(211001330)",bg='#085c74')
        about.gemmy = Label( about, text = "2- Abdelrahman Gamal Abd-El Fattah(211000869)",bg='#085c74')
        about.jemmy = Label( about, text = "3- Jumana Mohamed Ahmed(211002131)",bg='#085c74')
        about.tony = Label( about, text = "4- Anthony Atef Fikry(211000101)",bg='#085c74')
        about.button = Button( about, text = "Close", width = 25,
                                 command = self.close_window )
        
        about.title.pack()
        about.create.pack()
        about.marc.pack()
        about.gemmy.pack()
        about.jemmy.pack()
        about.tony.pack()
        about.button.pack(side=BOTTOM)
        
    #Close Function:
    def close_window(self):
        self.destroy()
#----------------


#Looping Part:
#----------------
def main(): 
    MainWin().mainloop()
if __name__ == '__main__':
    main()
#----------------