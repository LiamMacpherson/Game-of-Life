import tkinter as tk
from view import View as view
from model import Model as model
from random import randint

class Controller():
    def __init__(self):
            root = tk.Tk()
            self.gui = view.View(root, self)
            self.m = model.Model(self.gui)
            self.gui.show_window()
            self.pause = False

    def get_cell(self, x, y):
        return self.m.g.get_cell(x,y)

    def randomise(self):
        for x in range(9):
            for y in range(14):
                dead_or_alive = randint(0,1)
                self.get_cell(x,y).alive=dead_or_alive
                self.get_cell(x, y).next_state = dead_or_alive
        self.step


    def step(self):
        self.m.step()