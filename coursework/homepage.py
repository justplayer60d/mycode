from coursework import wordedalgebra
from coursework
from tkinter import *


class homepage:
    def __init__(self, window):
        # Store reference to the main window
        self.window = window
        self.worded_boolean_button = Button(window, text="worded boolean input",command=open_worded_boolean_page ,("Arial", 14, "bold")).pack(pady=10)
        self.karnaugh_map_button = Button(window, text="karnaugh map input",command=open_karnaugh_map_page, font=("Arial", 14, "bold")).pack(pady=15)


        # Set the title that appears at the top of the window
        window.title("Boolean Calculator")

        # display main heading label
        Label(window, text="boolean algebra and karnaugh map calculator", font=("Arial", 14, "bold")).pack(pady=20)
    def open_worded_boolean_page(self):
        print("y")
    def open_karnaugh_map_page(self):
        print("x")
window = Tk()
app = homepage(window)
window.mainloop()