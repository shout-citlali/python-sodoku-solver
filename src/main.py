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

#  Set up onkey listener for numbers 1 - 9, each needs a function in gameboard. Leverage active cell of gameboard. Space onkey to clear and user_defined = False
screen.onkey(game_board.input_1, "1")  # check syntax on number. in place of cell id, display cell number (in draw function), make it pretty 
screen.exitonclick()
# Test line
