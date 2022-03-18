from turtle import Turtle, Screen, update

from gameboard import Gameboard

graphics = Turtle()
screen = Screen()
game_board = Gameboard(graphics, screen)

game_board.draw()
print(game_board.cells)

screen.listen()
# screen.onkey(myFunc, "Up")
# screen.onkey(myFunc, "Down")
screen.onkey(game_board.cursor_left, "Left")
screen.onkey(game_board.cursor_right, "Right")

screen.exitonclick()