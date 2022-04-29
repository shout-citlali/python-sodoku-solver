from turtle import Turtle, Screen, update

from gameboard import Gameboard

graphics = Turtle()
screen = Screen()
game_board = Gameboard(graphics, screen)

game_board.draw()

screen.listen()
screen.onkey(game_board.cursor_up, "Up")
screen.onkey(game_board.cursor_down, "Down")
screen.onkey(game_board.cursor_left, "Left")
screen.onkey(game_board.cursor_right, "Right")

screen.exitonclick()
# Test line
