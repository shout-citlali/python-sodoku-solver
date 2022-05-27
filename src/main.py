from turtle import Turtle, Screen, update

from gameboard import Gameboard

graphics = Turtle()
screen = Screen()
game_board = Gameboard(graphics, screen)

game_board.extreme_setup()

game_board.draw()

screen.listen()
screen.onkey(game_board.cursor_up, "Up")
screen.onkey(game_board.cursor_down, "Down")
screen.onkey(game_board.cursor_left, "Left")
screen.onkey(game_board.cursor_right, "Right")
screen.onkey(game_board.input_1, "1")
screen.onkey(game_board.input_2, "2")
screen.onkey(game_board.input_3, "3")
screen.onkey(game_board.input_4, "4")
screen.onkey(game_board.input_5, "5")
screen.onkey(game_board.input_6, "6")
screen.onkey(game_board.input_7, "7")
screen.onkey(game_board.input_8, "8")
screen.onkey(game_board.input_9, "9")
screen.onkey(game_board.spacebar, "space")
screen.onkey(game_board.enter, "Return")

screen.exitonclick()
