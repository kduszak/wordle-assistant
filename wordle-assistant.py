import pandas as pd
from tkinter import *
from tkinter import ttk

# Saving csv file as pandas dataFrame
# TODO: words = list(pd.read_csv('wordles.csv'))

def analyse(*args):
    try:
        suggested_guess.set("OKAPI")
    except ValueError:
        pass

def charLimiter(box_contents):
    if len(box_contents) < 2:
        return True
    else:
        return False

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

suggested_guess = StringVar()
ttk.Label(mainframe, textvariable = suggested_guess).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = "Analyse", command = analyse).grid(column = 6, row = 3, sticky = W)




root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

first_letter_entry.focus()


root.mainloop()