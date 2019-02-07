import tkinter as tk
from view import Grid


class View:
    def __init__(self, root, c):
        self.window = root
        self.c = c
        # get the screen's dimensions
        self.s_width = self.window.winfo_screenwidth()
        self.s_height = self.window.winfo_screenheight()


    def show_window(self):
        # get the windows size
        w_width = 750
        w_height = 500
        # calculate the position of the top left corner of the window to be just above center of the user's screen
        pos_x = int(self.s_width/2 - w_width/2)
        pos_y = int(self.s_height/3 - w_height/2)

        self.grid_cont = tk.Frame(self.window)
        self.grid_cont.pack(side="top", padx=(50,50), pady=(100,50))

        self.g = Grid.Grid(self.grid_cont, self.c)


        controls = tk.Frame(self.window)
        controls.pack(side="bottom", pady=(0,20))
        self.build_controls(controls)


        self.window.geometry("750x500")
        self.window.geometry("+{}+{}".format(pos_x, pos_y))
        self.window.title("Game of Life")
        self.window.resizable(False, False)
        tk.mainloop()

    def get_width(self):
        return self.s_width

    def get_height(self):
        return self.s_height

    def exit(self):
        exit()

    def build_controls(self, controls):
        # Button to generate random seed
        randomise = tk.Button(controls, text="Randomise", command=lambda: self.c.randomise())
        randomise.pack(side="left", padx=25)
        # Button to step
        step = tk.Button(controls, text="Step", command=lambda: self.c.step())
        step.pack(side="left", padx=25)


