# IMPORT TURTLE GRAPHICS MODULE
import turtle

# DEFINE CONSTANTS
WIDTH = 500
HEIGHT = 500

# CREATE WINDOW WHERE TURTLE WILL DRAW
drawing_board = turtle.Screen()
drawing_board.setup(WIDTH, HEIGHT)
drawing_board.title("Stamping")
drawing_board.bgcolor("cyan")


# CREATE A TURTLE
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("yellow")
stamper.shapesize(50 / 20)  # SET STAMP TO 50PX
stamper.stamp()
stamper.penup()  # TO PREVENT MARKING WHILE MOVING
stamper.shapesize(10 / 20)
stamper.goto(100, 100)
stamper.stamp()


# LET THE TURTLE KNOW TO STOP
turtle.done()

