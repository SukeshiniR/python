import random
import curses

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)

# Get the heigh and the width of the screen
screen_height, screen_width = screen.getmaxyx()

# Initialize the window
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

# Initial position of the snake
snk_x = screen_width//4
snk_y = screen_height//2

# Initial size of the snake
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Initial food position on the screen
food = [screen_height//2, screen_width//2]

# The food will be denoted as 'X'
window.addch(food[0], food[1], "X")

# Initial key
key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # If height of snake is equals to the height of the screen or width of the snake is equals to the width of the
    # screen or snake's head touches his body, then stop the game
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # Define the new head
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # If snake reached the food
    if snake[0] == food:
        food = None
        while food is None:
            # Define new food in a random position on the screen
            new_food = [
                random.randint(1, screen_height-1),
                random.randint(1, screen_width-1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], "X")
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
