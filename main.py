# IMPORT TURTLE GRAPHICS MODULE
import turtle
import random

# DEFINE CONSTANTS
WIDTH = 500
HEIGHT = 500
DELAY = 200  # MILLISECONDS BETWEEN FRAME UPDATES
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "right": (20, 0),
    "down": (0, -20),
    "left": (-20, 0)
}


def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


# CREATE WINDOW WHERE TURTLE WILL DRAW
drawing_board = turtle.Screen()
drawing_board.setup(WIDTH, HEIGHT)
drawing_board.title("Snake")
drawing_board.bgcolor("cyan")
drawing_board.tracer(0)  # TURN OFF AUTO-ANIMATION

# EVENT HANDLERS
drawing_board.listen()
drawing_board.onkey(go_up, "Up")
drawing_board.onkey(go_right, "Right")
drawing_board.onkey(go_down, "Down")
drawing_board.onkey(go_left, "Left")

# CREATE A TURTLE
slithery_snake = turtle.Turtle()
slithery_snake.shape("square")
slithery_snake.color("yellow")
slithery_snake.penup()  # TO PREVENT MARKING WHILE MOVING

# CREATE SNAKE AS A LIST OF PAIRED COORDINATES
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

# DRAW INITIAL SNAKE
for segment in snake:
    slithery_snake.goto(segment[0], segment[1])
    slithery_snake.stamp()


# MOVE THE SNAKE
def game_loop():
    slithery_snake.clearstamps()  # GETS RID OF EXISTING SNAKE

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]  # INCREASE THE COPY'S X COORDINATE ACCORDING TO KEY PRESS
    new_head[1] += offsets[snake_direction][1]  # INCREASE THE COPY'S Y COORDINATE ACCORDING TO KEY PRESS

    # CHECK FOR COLLISIONS
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        turtle.bye()  # END THE GAME IF THE SNAKE COLLIDES WITH ITSELF OR THE EDGES
    else:
        # MOVE THE SNAKE
        snake.append(new_head)  # MOVE THE HEAD OF THE SNAKE

        # CHECK FOR FOOD COLLISION
        if not food_chomp():
            snake.pop(0)  # MAINTAIN SNAKE LENGTH / REMOVE LAST TAIL SEGMENT

        # DRAW THE SNAKE
        for segment in snake:
            slithery_snake.goto(segment[0], segment[1])
            slithery_snake.stamp()

    # REFRESH THE SCREEN
    drawing_board.update()

    # REPEAT THE PROCESS AS NECESSARY
    turtle.ontimer(game_loop, DELAY)


def food_chomp():
    """
    This function will check whether the snake has successfully eaten a food item.
    :return:
    """
    global food_spot
    if get_distance(snake[-1], food_spot) < 20:
        food_spot = get_random_food_spot()
        food.goto(food_spot)
        return True
    return False


def get_random_food_spot():
    # CONSTRAIN RANDOM FOOD PLACEMENT TO DIMENSIONS OF PLAYING AREA
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return x, y


def get_distance(position1, position2):
    """
    This function finds the distance between two points, for the purposes of working out whether the snake has
    successfully eaten the food.
    :param position1:
    :param position2:
    :return:
    """
    x1, y1 = position1
    x2, y2 = position2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # EQUIV. TO TAKING SQUARE ROOT (PYTHAGOREAN THEOREM)
    return distance


# FOOD
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food_spot = get_random_food_spot()
food.goto(food_spot)

# BEGIN ANIMATION
game_loop()

# STOP THE PROGRAM
turtle.done()
