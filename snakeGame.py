import random, curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
window = curses.newwin(sh, sw, 0, 0)
window.keypad(1)
window.timeout(100)

snake_x = snake_y = sw / 2

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [sh / 2, sw / 2]
window.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    nextKey = window.getch()
    key = key if nextKey == -1 else nextKey

    # game over
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    newHead = [snake[0][0], snake[0][1]]

    if key == curses.KEY_UP:
        newHead[0] += 1

    elif key == curses.KEY_DOWN:
        newHead[0] -= 1

    elif key == curses.KEY_RIGHT:
        newHead[1] += 1

    elif key == curses.KEY_LEFT:
        newHead[1] -= 1

    snake.insert(0, newHead)

    if snake[0] == food:
        food = False

        while food is False:
            newFood = [random.randint(1, sh - 1), random.randint(1, sw - 1)]
            food = True if newFood not in snake else False
        
        window.addch(food[0], food[1], curses.ACS_PI)
    
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')

    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
            