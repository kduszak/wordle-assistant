import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Saving csv file as pandas dataFrame
# TODO: words = list(pd.read_csv('wordles.csv'))

def analyse(*args):
    try:
        #for x in range(5):
            #print(letters[x].get())
            #print(buttons[x].cget("bg"))
        suggested_guess.set("OKAPI")
    except ValueError:
        pass

def charLimiter(box_contents):
    if len(box_contents) < 2:
        return True
    else:
        return False
    
colours = {0:"gray", 1:"yellow", 2:"green"}

def coloursLookup(target):
    for k in colours:
        if colours[k] == target:
            return k
        
def change_button_colour(button):
    new_colour = colours[(coloursLookup(button.cget("bg")) + 1)%3]
    button.config(bg = new_colour)

root = Tk()
root.title("Wordle Assistant")

charLimiter_call = root.register(charLimiter)

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))



first_letter = StringVar()
first_letter_entry = ttk.Entry(mainframe, width = 3, textvariable = first_letter, validate = "key", validatecommand = (charLimiter_call, '%P'))
first_letter_entry.grid(column = 1, row = 1, sticky = (W, E))
second_letter = StringVar()
second_letter_entry = ttk.Entry(mainframe, width = 3, textvariable = second_letter, validate = "key", validatecommand = (charLimiter_call, '%P'))
second_letter_entry.grid(column = 2, row = 1, sticky = (W, E))
third_letter = StringVar()
third_letter_entry = ttk.Entry(mainframe, width = 3, textvariable = third_letter, validate = "key", validatecommand = (charLimiter_call, '%P'))
third_letter_entry.grid(column = 3, row = 1, sticky = (W, E))
fourth_letter = StringVar()
fourth_letter_entry = ttk.Entry(mainframe, width = 3, textvariable = fourth_letter, validate = "key", validatecommand = (charLimiter_call, '%P'))
fourth_letter_entry.grid(column = 4, row = 1, sticky = (W, E))
fifth_letter = StringVar()
fifth_letter_entry = ttk.Entry(mainframe, width = 3, textvariable = fifth_letter, validate = "key", validatecommand = (charLimiter_call, '%P'))
fifth_letter_entry.grid(column = 5, row = 1, sticky = (W, E))
letters = (first_letter, second_letter, third_letter, fourth_letter, fifth_letter)

first_letter_button = tk.Button(mainframe, bg = "gray", command = lambda: change_button_colour(first_letter_button))
first_letter_button.grid(column = 1, row = 2, sticky = EW)

second_letter_button = tk.Button(mainframe, bg = "gray", command = lambda: change_button_colour(second_letter_button))
second_letter_button.grid(column = 2, row = 2, sticky = EW)

third_letter_button = tk.Button(mainframe, bg = "gray", command = lambda: change_button_colour(third_letter_button))
third_letter_button.grid(column = 3, row = 2, sticky = EW)

fourth_letter_button = tk.Button(mainframe, bg = "gray", command = lambda: change_button_colour(fourth_letter_button))
fourth_letter_button.grid(column = 4, row = 2, sticky = EW)

fifth_letter_button = tk.Button(mainframe, bg = "gray", command = lambda: change_button_colour(fifth_letter_button))
fifth_letter_button.grid(column = 5, row = 2, sticky = EW)
buttons = (first_letter_button, second_letter_button, third_letter_button, fourth_letter_button, fifth_letter_button)

suggested_guess = StringVar()
ttk.Label(mainframe, textvariable = suggested_guess).grid(column = 6, row = 4, sticky = (W, E))

ttk.Button(mainframe, text = "Analyse", command = analyse).grid(column = 6, row = 3, sticky = W)




root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

first_letter_entry.focus()


root.mainloop()