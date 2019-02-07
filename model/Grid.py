from model import Cell

class Grid:
    def __init__(self, v):
        # Width and Height passed in as cells
        self.view = v
        self.width = 10
        self.height = 15
        self.number_of_cells = self.width * self.height
        # Create a 2D array of cells
        self.grid = [[Cell.Cell(x,y) for y in range(self.height)] for x in range(self.width)]

    def add_neighbours(self):
        for row in self.grid:
            for cell in row:
                for x in range(-1,2):
                    for y in range(-1,2):

                        #get the position of the possible new neighbour
                        n_x = cell.x + x
                        n_y = cell.y + y

                        # neighbour is a cell out of the grid
                        if n_x < 0 or n_x >= self.width or n_y < 0 or n_y >= self.height:
                            continue

                        # new neighbour would be the same cell
                        if self.grid[n_x][n_y] == cell:
                            continue
                        cell.add_neighbour(self.grid[n_x][n_y])

    def update_grid(self):
        x = 0
        for row in self.grid:
            y = 0
            for cell in row:
                if not cell.alive and cell.next_state:
                    self.view.grid_cont.grid_slaves(x, y)[0].grid_forget()
                    cell.alive = cell.next_state
                elif cell.alive and not cell.next_state:
                    self.view.g.make_button(x,y)
                    cell.alive = cell.next_state
                y += 1
            x += 1

    def evolve(self):
        for row in self.grid:
            for cell in row:
                cell.evolve()

    def get_cell(self, x, y):
        if x < 0 or x > self.width or y < 0 or y > self.height:
            return False
        else:
            return self.grid[x][y]
