import curses
#import pingo
import time
import random

paddle_1_pos = 0, 10
paddle_2_pos = 79, 10

PADDLE_SIZE = 5
MIN_X = 0
MIN_Y = 0
MAX_X = 79
MAX_Y = 24

score_1 = 0
score_2 = 0

def init_ball():
    return ([39, 12], 
        random.choice([
        #[1, 0], 
        [1, 1], #[-1, 0], 
        [-1, 1], [1, -1]]))

def new_ball_pos(pos, velocity):
    x = pos[0] + velocity[0]
    y = pos[1] + velocity[1]
    return (x, y)

def paddle_collision(ball_pos, paddle_pos, paddle_size):
    return (ball_pos[0] == paddle_pos[0] and
             paddle_pos[1] <= ball_pos[1] <= paddle_pos[1] + PADDLE_SIZE) 

def draw_paddle(x, y, color):
    for offset in range(PADDLE_SIZE):
        screen.addstr(y + offset, x, ' ', color)

if __name__ == '__main__':

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    try:
        curses.curs_set(False)
    except:
        pass
    screen.clear()
    curses.start_color()

    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    ball_pos, ball_velocity = init_ball()

    while True:
        paddle_1_pos = 10
        paddle_2_pos = 10

        screen.addstr(ball_pos[1], ball_pos[0], ' ', curses.color_pair(2))

        draw_paddle(MIN_X, paddle_1_pos, curses.color_pair(2))
        draw_paddle(MAX_X, paddle_2_pos, curses.color_pair(2))

        # If left border collision, increase score and invert vx
        if ball_pos[0] <= MIN_X:
            ball_velocity[0] = - ball_velocity[0]
            # Check whether we collided with a paddle
            if not paddle_1_pos < ball_pos[1] < paddle_1_pos + PADDLE_SIZE:
                ball_pos, ball_velocity = init_ball()
       
        # If right border collision, increase score and invert vx
        if ball_pos[0] >= MAX_X:
            ball_velocity[0] = - ball_velocity[0]
            # Check whether we collided with a paddle
            if not paddle_1_pos < ball_pos[1] < paddle_1_pos + PADDLE_SIZE:
                ball_pos, ball_velocity = init_ball()
        
        # If top or botton collision, invert vy
        if not MIN_Y < ball_pos[1] < MAX_Y:
            ball_velocity[1] = - ball_velocity[1]
        
        ball_pos = new_ball_pos(ball_pos, ball_velocity)

        screen.addstr(ball_pos[1], ball_pos[0], ' ', curses.color_pair(1))
        draw_paddle(MIN_X, paddle_1_pos, curses.color_pair(1))
        draw_paddle(MAX_X, paddle_2_pos, curses.color_pair(1))

        screen.refresh()
        
        time.sleep(0.05)
        
        
