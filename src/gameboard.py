from cell import Cell


class Gameboard:
    def __init__(self, graphics, screen):
        self.graphics = graphics
        self.screen = screen
        self.screen.setworldcoordinates(0, 1100, 1100, 0)
        self.screen.title("Sudoku Solver")
        self.screen.tracer(0)
        self.cells = []
        for row in range(0, 9):
            for col in range(0, 9):
                self.cells.append(Cell(row, col))
        for cell in self.cells:
            cell.east = self.cells[cell.id - 8 if (cell.id + 1) % 9 == 0 else cell.id + 1]
            # cell.west = self.cells[cell.id + 9 if cell.id % 9 == 0 else cell.id]  # determine what cell west should be
        self.active_cell = self.cells[0]

    def draw(self):
        self.graphics.clear()
        self.graphics.hideturtle()
        self.graphics.width(3)
        for x in range(1, 11):
            self.graphics.penup()
            self.graphics.goto(100, 100 * x)
            self.graphics.pendown()
            self.graphics.forward(900)
            self.graphics.right(90)
            self.graphics.setheading(90)
            self.graphics.penup()
            self.graphics.goto(100 * x, 100)
            self.graphics.pendown()
            self.graphics.forward(900)
            self.graphics.setheading(0)
        self.graphics.penup()
        self.graphics.goto(110 + 100 * self.active_cell.column_id, 110 + 100 * self.active_cell.row_id)
        self.graphics.pendown()
        for i in range(4):
            self.graphics.forward(80)
            self.graphics.left(90)
        self.graphics.penup()
        for cell in self.cells:
            self.graphics.goto(cell.column_id * 100 + 150, cell.row_id * 100 + 165,)
            self.graphics.write(cell.id, move=False, align="center", font=("Arial", 12, "normal"))
            self.graphics.goto(cell.column_id * 100 + 180, cell.row_id * 100 + 165)
            self.graphics.write(cell.east.id, move=False, align="center", font=("Arial", 8, "normal"))
            self.graphics.goto(cell.column_id * 100 - 80, cell.row_id * 100 - 65)
            # self.graphics.write(cell.west.id, move=False, align="center", font=("Arial", 8, "normal"))# print west neighbor on left side of each square
        self.screen.update()

    def cursor_right(self):
        self.active_cell = self.active_cell.east
        self.draw()

    def cursor_left(self):
        self.active_cell = self.active_cell.west
        self.draw()
