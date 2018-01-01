#This is a simple text editor using Tkinter, one of the standard python GUI package
#python version: Python 3.6.3
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

filename = None

def NewFile():
    global filename #this need to be defined like this in order to modify global variable. we can use directly without 'global' for read-only purpose
    filename = "untitled"
    text.delete(0.0, END)   #0.0: zero before period indicates line number and zero after period indicates column number
                            #text.delete(0.0, END) deletes everything from first line first column to the END

def SaveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def SaveAs():
    f = asksaveasfile(defaultextension = '.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip()) #t.strip(): Return a copy of the string with the leading and trailing characters removed
    except:                 #t.rstrip(): Returns copy of string with trailing character removed. t.lstrip() for leading characters
        showerror(title = 'ERROR', message = 'Unable to save file')

root =Tk()

def OpenFile():
    global filename
    f = askopenfile(parent=root, title = 'Select a file')
    filename = f.name
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    f.close()

root.title("mero-text")
root.minsize(width = 480, height=480)
root.maxsize(width = 480, height=480)

text = Text(root, width = 480, height = 480)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', command = NewFile)
filemenu.add_command(label = 'Open', command = OpenFile)
filemenu.add_command(label = 'Save', command = SaveFile)
filemenu.add_command(label = 'Save as..', command = SaveAs)
filemenu.add_separator()
filemenu.add_command(label = 'Quit', command = root.quit)
menubar.add_cascade(label = 'File', menu = filemenu)

root.config(menu = menubar)
root.mainloop()
