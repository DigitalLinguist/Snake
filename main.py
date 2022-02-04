# IMPORT NECESSARY MODULES
import turtle
import random

# DEFINE CONSTANTS
WIDTH = 650
HEIGHT = 650
DELAY = 200  # MILLISECONDS BETWEEN FRAME UPDATES
FOOD_SIZE = 25

offsets = {
    "up": (0, 20),
    "right": (20, 0),
    "down": (0, -20),
    "left": (-20, 0)
}


def bind_direction_keys():
    drawing_board.onkey(lambda: set_snake_direction("up"), "Up")
    drawing_board.onkey(lambda: set_snake_direction("right"), "Right")
    drawing_board.onkey(lambda: set_snake_direction("down"), "Down")
    drawing_board.onkey(lambda: set_snake_direction("left"), "Left")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":     # AVOID COLLISION BY WRONG KEY PRESS
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":     # AVOID COLLISION BY WRONG KEY PRESS
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":     # AVOID COLLISION BY WRONG KEY PRESS
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":     # AVOID COLLISION BY WRONG KEY PRESS
            snake_direction = "right"


# MOVE THE SNAKE
def game_loop():
    slithery_snake.clearstamps()  # GETS RID OF EXISTING SNAKE

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]  # INCREASE THE COPY'S X COORDINATE ACCORDING TO KEY PRESS
    new_head[1] += offsets[snake_direction][1]  # INCREASE THE COPY'S Y COORDINATE ACCORDING TO KEY PRESS

    # CHECK FOR COLLISIONS
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset_snake()  # END THE GAME IF THE SNAKE COLLIDES WITH ITSELF OR THE EDGES
    else:
        # MOVE THE SNAKE
        snake.append(new_head)  # MOVE THE HEAD OF THE SNAKE

        # CHECK FOR FOOD COLLISION
        if not food_chomp():
            snake.pop(0)  # MAINTAIN SNAKE LENGTH / REMOVE LAST TAIL SEGMENT UNLESS FED

        # DRAW THE SNAKE
        for segment in snake:
            slithery_snake.goto(segment[0], segment[1])
            slithery_snake.stamp()

    # REFRESH THE SCREEN
    drawing_board.title(f"Snake Game: Your Score is {score}!")
    drawing_board.update()

    # REPEAT THE PROCESS AS NECESSARY
    turtle.ontimer(game_loop, DELAY)


def food_chomp():
    """
    This function will check whether the snake has successfully eaten a food item.
    :return:
    """
    global food_spot, score
    if get_distance(snake[-1], food_spot) < 20:
        score += 1          # increment score
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


def reset_snake():
    global score, snake, snake_direction, food_spot

    # CALIBRATE SCOREBOARD
    score = 0

    # CREATE SNAKE AS A LIST OF PAIRED COORDINATES
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"

    # GENERATE FOOD
    food_spot = get_random_food_spot()
    food.goto(food_spot)

    game_loop()


# CREATE WINDOW WHERE TURTLE WILL DRAW
drawing_board = turtle.Screen()
drawing_board.setup(WIDTH, HEIGHT)
drawing_board.title("Snake")
drawing_board.bgcolor("yellow")
drawing_board.tracer(0)  # TURN OFF AUTO-ANIMATION


# EVENT HANDLERS
drawing_board.listen()
bind_direction_keys()


# CREATE A TURTLE
slithery_snake = turtle.Turtle()
slithery_snake.shape("square")
slithery_snake.color("cyan")
slithery_snake.penup()  # TO PREVENT MARKING WHILE MOVING


# FOOD
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(FOOD_SIZE / 20)
food.penup()


# BEGIN ANIMATION
reset_snake()

# STOP THE PROGRAM
turtle.done()
