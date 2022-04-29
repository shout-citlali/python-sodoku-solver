from cell import Cell
import math


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
            cell.west = self.cells[cell.id + 8 if cell.id % 9 == 0 else cell.id - 1]
            cell.north = self.cells[cell.id + 72 if cell.id < 9 else cell.id - 9]
            cell.south = self.cells[cell.id - 72 if cell.id > 71 else cell.id + 9]
            row_start_id = cell.id - cell.id % 9
            col_start_id = cell.id % 9
            grid_start_id = cell.id - (cell.id % 27) + (cell.id % 9) - (cell.id % 3)
            for i in range(0, 9):
                if row_start_id + i != cell.id:
                    cell.row_associations.append(self.cells[row_start_id + i])
                if col_start_id + (i * 9) != cell.id:
                    cell.column_associations.append(self.cells[col_start_id + i * 9])
                if grid_start_id + (i % 3) + (math.floor(i / 3) * 9) != cell.id:
                    cell.grid_associations.append(self.cells[grid_start_id + (i % 3) + (math.floor(i / 3) * 9)])
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

        self.graphics.goto(105 + 100 * self.active_cell.column_id, 105 + 100 * self.active_cell.row_id)
        self.graphics.color("blue")
        self.graphics.pendown()
        for i in range(4):
            self.graphics.forward(90)
            self.graphics.left(90)
        self.graphics.penup()
        self.graphics.color("black")

        for cell in self.active_cell.row_associations + self.active_cell.column_associations + self.active_cell.grid_associations:
            self.graphics.goto(105 + 100 * cell.column_id, 105 + 100 * cell.row_id)
            self.graphics.color("yellow")
            self.graphics.pendown()
            for i in range(4):
                self.graphics.forward(90)
                self.graphics.left(90)
            self.graphics.penup()
            self.graphics.color("black")

        for cell in self.cells:
            self.graphics.goto(cell.column_id * 100 + 150, cell.row_id * 100 + 165,)
            self.graphics.write(cell.id, move=False, align="center", font=("Arial", 12, "normal"))
            self.graphics.goto(cell.column_id * 100 + 180, cell.row_id * 100 + 165)
            self.graphics.write(cell.east.id, move=False, align="center", font=("Arial", 8, "normal"))
            self.graphics.goto(cell.column_id * 100 + 120, cell.row_id * 100 + 165)
            self.graphics.write(cell.west.id, move=False, align="center", font=("Arial", 8, "normal"))
            self.graphics.goto(cell.column_id * 100 + 150, cell.row_id * 100 + 130)
            self.graphics.write(cell.north.id, move=False, align="center", font=("Arial", 8, "normal"))
            self.graphics.goto(cell.column_id * 100 + 150, cell.row_id * 100 + 190)
            self.graphics.write(cell.south.id, move=False, align="center", font=("Arial", 8, "normal"))
        self.screen.update()


    def cursor_right(self):
        self.active_cell = self.active_cell.east
        self.draw()


    def cursor_left(self):
        self.active_cell = self.active_cell.west
        self.draw()


    def cursor_up(self):
        self.active_cell = self.active_cell.north
        self.draw()


    def cursor_down(self):
        self.active_cell = self.active_cell.south
        self.draw()