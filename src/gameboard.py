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
            if cell.has_conflicts() > 0:
                self.graphics.color("red")
            self.graphics.goto(cell.column_id * 100 + 150, cell.row_id * 100 + 195,)
            self.graphics.write("" if cell.number == None else cell.number, move=False, align="center", font=("Arial", 40, "normal"))
            self.graphics.color("black")
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


    def input_1(self):
        self.active_cell.number = 1
        self.active_cell.user_defined = True
        self.draw()

    def input_2(self):
        self.active_cell.number = 2
        self.active_cell.user_defined = True
        self.draw()

    def input_3(self):
        self.active_cell.number = 3
        self.active_cell.user_defined = True
        self.draw()

    def input_4(self):
        self.active_cell.number = 4
        self.active_cell.user_defined = True
        self.draw()

    def input_5(self):
        self.active_cell.number = 5
        self.active_cell.user_defined = True
        self.draw()

    def input_6(self):
        self.active_cell.number = 6
        self.active_cell.user_defined = True
        self.draw()

    def input_7(self):
        self.active_cell.number = 7
        self.active_cell.user_defined = True
        self.draw()

    def input_8(self):
        self.active_cell.number = 8
        self.active_cell.user_defined = True
        self.draw()

    def input_9(self):
        self.active_cell.number = 9
        self.active_cell.user_defined = True
        self.draw()

    def spacebar(self):
        self.active_cell.number = None
        self.active_cell.user_defined = False
        self.draw()

    def enter(self):
        print("Unable to solve puzzle")

    def performSetup(self, config):
        for i, c in enumerate(config):
            if c is not None:
                self.cells[i].number = c
                self.cells[i].user_defined = True


    def gentleSetup(self):
        setup = [
            4, None, 1, None, 5, None, 6, None, 3,
            None, 2, None, 1, None, 7, None, 4, 5,
            6, None, 7, None, 3, None, 1, None, None,
            5, None, 2, 3, None, 8, 9, None, 1,
            None, 1, None, 2, 9, 5, None, 3, None,
            3, None, 8, 6, None, 1, 7, None, 2,
            None, None, 9, None, 2, None, 5, None, 7,
            8, 6, None, 7, None, 3, None, 9, None,
            2, None, 4, None, 8, None, 3, None, 6,
        ]
        self.performSetup(setup)

    def easySetup(self):
        setup = [
            None, None, None, 5, None, 4, 7, None, None,
            None, None, None, 3, 9, 6, 2, None, None,
            5, 3, 2, None, 8, None, 4, None, None,
            6, None, None, 7, None, 8, None, 2, None,
            None, 8, 1, None, None, None, 5, 9, None,
            None, 2, None, 9, None, 5, None, None, 7,
            None, None, 4, None, 7, None, 6, 3, 1,
            None, None, 6, 2, 4, 3, None, None, None,
            None, None, 8, 6, None, 1, None, None, None,
        ]
        self.performSetup(setup)

    def MediumSetup(self):
        setup = [
            None, None, None, None, 1, None, None, 3, 8,
            None, None, 7, 4, None, None, None, None, None,
            None, 5, None, None, None, None, None, None, 2,
            None, 2, None, 7, None, None, 5, None, None,
            8, 7, None, None, 3, None, None, 6, 1,
            None, None, 9, None, None, 6, None, 8, None,
            3, None, None, None, None, None, None, 1, None,
            None, None, None, None, None, 9, 6, None, None,
            2, 4, None, None, 8, None, None, None, None,
        ]
        self.performSetup(setup)

        



