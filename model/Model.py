from model import Grid

class Model:
    def __init__(self, v):
        # Pass the view into the grid to allow the model to update
        self.g = Grid.Grid(v)
        self.g.add_neighbours()

    def step(self):
        self.g.evolve()
        self.g.update_grid()

