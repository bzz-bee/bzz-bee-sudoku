from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import tkinter
import numpy as np
import sudokum

g = sudokum.generate(mask_rate=0.7)

gui_bg_color = '#2d8091'
cell_color = '#d3d3d3'
active_color = '#66aacc'
input_num_color= '#28aa28'
gui = Tk()
gui.title("Sudoku")
gui.geometry('1200x1500')
gui.configure(bg=gui_bg_color)

def Restart():
    for cell in inputs:
        cell.configure(text=" ") 

def About():
    messagebox.showinfo(title='About', message='Created by bzz_bee with help from sudobeans. Version 0.1 released May 19th, 2024. Thank you!')

optionS = ttk.Style()
optionS.configure('O.TButton', font=('monospace', 20), width=9)
menuframe = ttk.Frame(gui, width=1200, height=36)
menuframe.pack(side='bottom')
newgameB = ttk.Button(menuframe, text='New Game', style='O.TButton')

restartB = ttk.Button(menuframe, text='Restart', style='O.TButton', command=Restart)
restartB.pack(side='left')
aboutB = ttk.Button(menuframe, text='About', style='O.TButton', command=About)
aboutB.pack(side='left')

mainframe = ttk.Frame(gui, borderwidth=27, relief="ridge")
mainframe.place(x=190, y=90)
mainframe.rows = 3
mainframe.cols = 3
mainframe.grid = np.empty(shape=(mainframe.rows, mainframe.cols), dtype=object)

inputS = ttk.Style()
inputS.configure('I.TButton', font=('monospace', 40, 'bold'), 
            borderwidth='3', width=2, background=cell_color, foreground=input_num_color)
inputs = []

activeB = None
def on_enter(e: tkinter.Event):
    global activeB
    activeB = e.widget

def on_leave(e: tkinter.Event):
    global activeB
    activeB = None

def key_press(a):
    global activeB
    if activeB is not None:
        activeB.configure(text=a.char)
        inputs.append(activeB)

def backspace(e: tkinter.Event):
    global activeB
    if activeB is not None:
        activeB.configure(text=" ")

for w in range(mainframe.rows):
    for x in range(mainframe.cols):
        subframe = ttk.Frame(mainframe, width=240, height=240, borderwidth=9, relief='ridge')
        subframe.rows = 3
        subframe.cols = 3
        subframe.grid(column=w, row=x)

        cellS = ttk.Style()
        cellS.configure('C.TButton', font=('monospace', 40, 'bold'), borderwidth='3', 
                        width=2, background=cell_color)

        for y in range(subframe.rows):
            for z in range(subframe.cols):
                cell = ttk.Button(subframe, style='C.TButton')
                cell.grid(column=z, row=y)
                cells = []
                cells.append(cell)
                row = 3 * x + y
                col = 3 * w + z
                cell.configure(text=g[row][col])
                if g[row][col] == 0:
                    cell.configure(text=" ", style='I.TButton')
                if g[row][col] != 0:
                    cell.configure(state='readonly')

                for i in range(10):
                    gui.bind(str(i), key_press)
                cell.bind('<Enter>', on_enter)
                cell.bind('<Leave>', on_leave)
                cell.bind('<BackSpace>', backspace)

gui.mainloop()
