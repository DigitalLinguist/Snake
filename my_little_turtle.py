# IMPORT TURTLE GRAPHICS MODULE
import turtle

# DEFINE CONSTANTS
WIDTH = 500
HEIGHT = 500
DELAY = 20  # MILLISECONDS BETWEEN SCREEN UPDATES

def move_turtle():
    little_turtle.forward(1)
    little_turtle.right(1)
    drawing_board.update()
    drawing_board.ontimer(move_turtle, DELAY)

# CREATE WINDOW WHERE TURTLE WILL DRAW
drawing_board = turtle.Screen()
drawing_board.setup(WIDTH, HEIGHT)
drawing_board.title("My Little Turtle")
drawing_board.bgcolor("yellow")
drawing_board.tracer(False)  # TURNS OFF AUTO-ANIMATION

# CREATE A TURTLE
little_turtle = turtle.Turtle()
little_turtle.shape("turtle")
little_turtle.color("blue")

# THE TURTLE NEEDS TO KNOW WHAT TO DO
move_turtle()

# LET THE TURTLE KNOW TO STOP
turtle.done()

