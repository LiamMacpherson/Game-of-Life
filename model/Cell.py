class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False
        self.neighbours = []
        self.next_state = False

    def evolve(self):
        n = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                n += 1

        #scenario 1/2
        if self.alive and (n > 3 or n < 2):
            self.kill()

        #scenario 3/4
        elif n == 3 or (self.alive and n == 2):
            self.live()

        #scenario 0
        else:
            self.kill()


    def kill(self):
        self.next_state = False

    def live(self):
        self.next_state = True

    def update(self):
        if(self.next_state != "w"):
            self.alive = self.next_state
        self.next_state = "w"

    def add_neighbour(self, cell):
        self.neighbours.append(cell)
