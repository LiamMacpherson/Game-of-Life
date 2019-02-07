import tkinter as tk
from model import Grid as mg

class Grid:
    def __init__(self, grid_frame, c):
        self.c = c
        self.grid_frame = grid_frame
        for x in range(10):
            for y in range(15):
                live_cell = tk.Frame(self.grid_frame, bg="red", height=20, width=20)
                live_cell.grid(row=x, column=y)
                button = tk.Button(self.grid_frame, relief="solid", text="")
                button.config(height=1, width=2, command=lambda x=x, y=y, button=button: self.clicked(x,y, button))
                button.grid(row=x, column=y)

    def clicked(self, x, y, button):
        button.grid_forget()
        #in inital state, user can select the buttons, thus the view enacts change on the model through the controller
        cell = self.c.get_cell(x, y)
        cell.alive=True


    def make_button(self,x,y):
        button = tk.Button(self.grid_frame, relief="solid", text="")
        button.config(height=1, width=2,command=lambda: self.clicked(x, y, button))
        button.grid(row=x, column=y)
        self.c.get_cell(x,y).alive = False

