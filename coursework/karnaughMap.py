import tkinter as tk
from tkinter import *

# create main window
root = tk.Tk()
root.title("Karnaugh Map")


# flips button between 0 and 1 when clicked
def circle_change(button):
    current = button.cget("text")  # get current value of button
    button.config(text="1" if current == "0" else "0")  # swap 0 to 1 or 1 to 0


cells_location = []
cell_store = []


def get_expression():
    store_cells_location = []
    for cell, row, col in cell_store:  # checking for those variables inside the array carrying all the cells
        if cell.cget("text") == "1":  # checking if the cell is TRUE
            location_of_1 = (row, col)  # stores the location of the row and column in a list
            store_cells_location.append(location_of_1)  # appends the lists into an array
    print(store_cells_location)


def num_of_variables():
    del cell_store[:]  # wipe cell_store before building new grid

    num = int(choose_num_of_variables.get())  # read entry box and convert to int

    # pick the correct headers depending on how many variables
    if num == 4:
        variables = ["C/D, A/B", "00", "01", "10", "11"]  # 4 variable kmap headers
    elif num == 3:
        variables = ["A/B, C", "00", "01", "11", "10"]  # 3 variable kmap headers
    elif num == 2:
        variables = ["A, C", "0", "1"]  # 2 variable kmap headers
    else:
        return  # stop function if number is not 2, 3 or 4

    # place header labels across the top row
    for col in range(len(variables)):
        cell = tk.Label(root, text=variables[col],
                        borderwidth=1, relief="solid",
                        width=8, height=3)
        cell.grid(row=1, column=col, padx=1, pady=1)

    # place side labels down the left column
    size = len(variables) - 1  # number of rows/cols needed for the grid
    for row in range(1, size + 1):
        cell = tk.Label(root, text=variables[row],
                        borderwidth=1, relief="solid",
                        width=8, height=3)
        cell.grid(row=row + 1, column=0, padx=1, pady=1)

    # fill the grid with clickable toggle buttons
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            cell = tk.Button(root, text="0",  # all cells start at 0
                             borderwidth=1, relief="solid",
                             width=8, height=3)
            # lambda passes the specific button so it toggles itself and not the last button made
            cell.config(command=lambda b=cell: circle_change(b))
            cell.grid(row=row + 1, column=col, padx=1, pady=1)
            cell_store.append((cell, row, col))



class Table:
    def __init__(self, root, lst):
        self.cells = []  # Store all Entry widgets in a 2D list to keep track of the table structure

        # Loop through each row in the data
        for i in range(len(lst)):
            row_cells = []  # Create empty list to store Entry widgets for this row

            # Loop through each column in the current row
            for j in range(len(lst[i])):
                # Create an Entry widget (editable text box) for this cell
                e = Entry(
                    root,  # Parent window where this Entry will be placed
                    width=20,  # Width of the text box in characters
                    fg='blue',  # Text color is blue
                    font=('Arial', 16, 'bold')  # Font style, size, and weight
                )
                # Place the Entry widget in a grid at row i, column j
                e.grid(row=i, column=j)
                # Insert the data value into the Entry widget at the end position
                e.insert(END, lst[i][j])
                # Add this Entry widget to the current row's list
                row_cells.append(e)
            # Add the completed row to the main cells list
            self.cells.append(row_cells)



def assining_the_values(n):  # function for assigning the truth table numbers to each variable
    # number of variables
    all_variables = ["A", "B", "C", "D"]  # list of the variables available
    variables = []
    for i in range(n):
        variables.append(all_variables[i])

    # values for respective num of variables
    if n == 2:
        values = [  # list of all numbers to be used for the truth table combination
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1)
        ]
    elif n == 3:
        values = [
            (0, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (0, 1, 1),
            (1, 0, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1)
        ]
    elif n == 4:
        values = [
            (0, 0, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
            (0, 0, 1, 1),
            (0, 1, 0, 0),
            (0, 1, 0, 1),
            (0, 1, 1, 0),
            (0, 1, 1, 1),
            (1, 0, 0, 0),
            (1, 0, 0, 1),
            (1, 0, 1, 0),
            (1, 0, 1, 1),
            (1, 1, 0, 0),
            (1, 1, 0, 1),
            (1, 1, 1, 0),
            (1, 1, 1, 1)
        ]

    dictonary = []
    for row in values:
        each_row = dict(zip(variables,
                            row))  # zip pairs each item in variables with the corresponding item in row, dict converts those pairs into a dictionary
        dictonary.append(each_row)
    return dictonary


def kmap_to_truth_table():
    # Get which cells are 1
    store_cells_location = []
    for cell, row, col in cell_store:
        if cell.cget("text") == "1":
            store_cells_location.append((row, col))

    # Get number of variables
    num = int(choose_num_of_variables.get())

    # USE assining_the_values
    dictonary = assining_the_values(num)#returns dictionary depending on the number of variables

    # Get variable names
    all_variables = ["A", "B", "C", "D"]
    variables = []
    for i in range(num):
        variables.append(all_variables[i])

    # Get values list
    values = []
    for row in dictonary:
        val_tuple = tuple(row[v] for v in variables)
        values.append(val_tuple)

    # Map K-map position to truth table index (using Gray code)
    kmap_to_index = {}

    # empty dictionary to store the kmap position as key and truth table row number as value
    kmap_to_index = {}

    if num == 2:
        # 2 variable kmap is a simple 2x2 grid so no translation needed
        # just calculate the index normally using row and column
        for kmap_row in range(1, 3):
            for kmap_col in range(1, 3):
                truth_table_index = (kmap_row - 1) * 2 + (kmap_col - 1)
                kmap_to_index[(kmap_row, kmap_col)] = truth_table_index

    elif num == 3:
        # kmap columns dont go in the same order as the truth table
        # this dictionary translates each kmap column number to the correct truth table position
        col_translation = {1: 0, 2: 1, 3: 3, 4: 2}

        # loop through all 2 rows and 4 columns of the 3 variable kmap
        for kmap_row in range(1, 3):
            for kmap_col in range(1, 5):
                # multiply row by 4 because there are 4 columns, then add translated column
                truth_table_index = (kmap_row - 1) * 4 + col_translation[kmap_col]
                # store the kmap position and its matching truth table row number
                kmap_to_index[(kmap_row, kmap_col)] = truth_table_index

    elif num == 4:
        # 4 variable kmap is 4x4 so both rows and columns need translating
        row_translation = {1: 0, 2: 1, 3: 3, 4: 2}
        col_translation = {1: 0, 2: 1, 3: 3, 4: 2}

        # loop through all 4 rows and 4 columns of the 4 variable kmap
        for kmap_row in range(1, 5):
            for kmap_col in range(1, 5):
                # translate both row and column then combine them into one index
                truth_table_index = row_translation[kmap_row] * 4 + col_translation[kmap_col]
                kmap_to_index[(kmap_row,
                               kmap_col)] = truth_table_index  # BUG: indented too far, python throws IndentationError and the whole program refuses to run

    # Build result column
    results = [0] * len(values)
    for loc in store_cells_location:
        if loc in kmap_to_index:
            results[kmap_to_index[loc]] = 1


    table_data = [variables + ['Result']]
    for val, res in zip(values, results):#had looked up the function zip
        row_data = list(val) + [res]
        table_data.append(row_data)


    table_window = Toplevel(root) #used the internet for the function toplevel
    table_window.title("Truth Table from K-map")

    t = Table(table_window, table_data)


# label and entry box for user to type number of variables
tk.Label(root, text="Num of variables:").grid(row=0, column=0, padx=10, pady=20)
choose_num_of_variables = tk.Entry(root, width=20)
choose_num_of_variables.grid(row=0, column=1, columnspan=4, padx=10, pady=20)

# create karnaugh map button calls num_of_variables to draw the kmap
tk.Button(root, text="create Karnaugh map", command=num_of_variables).grid(row=0, column=5, padx=10)

# output button - converts to truth table
tk.Button(root, text="Convert to Truth Table", command=kmap_to_truth_table).grid(row=0, column=6, padx=10)

# start the app and keep window open
root.mainloop()