# Example code for the drill

import pingo
import time
import sys

board = pingo.ghost.GhostBoard('foo.json') # gets an instance of your board's driver

# this is equivalent to init_io from your code
a_rotation = board.pins[12]               # this pin controls a relay that turns the drill on/off
a_direction = board.pins[13]              # defines which direction the drill will move up/down
a_move = board.pins[14]                   # turns on the drill's actuators

s_on = board.pins[9]                      # on/off switch that the user presses
s_down = board.pins[10]                   # Bottom switch
s_up = board.pins[11]                     # Top switch

a_rotation.mode = pingo.OUT
a_direction.mode = pingo.OUT
a_move.mode = pingo.OUT

s_on.mode = pingo.IN
s_down.mode = pingo.IN
s_up.mode = pingo.IN

if __name__ == '__main__':
    # this is equivalent to affect_outputs, read_inputs from your code
    m_state = 1                          # Using the finite-state machine abstraction
    step, max_steps = 0, 10              # From your code

    while True:                          # Loop function from your code
        # resets the drill to the initial position
        a_direction.lo()                 # Sets the drill to go up
        a_rotation.lo()                  # Turns the drill off
        while not s_up.state == pingo.HIGH:
            a_move.hi()                  # Moves the drill down
            time.sleep(1)
        a_move.low()                     # Stops moving

        # This inner loop represents the working cicle.
        while s_on.state == pingo.HIGH:
            if m_state == 1:
                a_rotation.hi()          # Turns the drill on
                a_direction.hi()         # Sets the drill to go down
                a_move.hi()              # Moves the drill down

                if s_down.state == pingo.HIGH:
                    m_state = 2          # if the drill presses s_down, we go to the next m_state
                    step += 1            # Counts the numbers of steps
                    break

            elif m_state == 2:
                a_rotation.hi()          # Turns the drill on
                a_direction.lo()         # Sets the drill to go up
                a_move.hi()              # Moves the drill up

                if s_up.state == pingo.HIGH:
                    m_state = 1          # if the drill presses s_up, we go to the previous m_state
                    step += 1            # Counts the numbers of steps
                    break

            time.sleep(1)

        time.sleep(1)
        if step < max_steps:
            pass
            #sys.exit()

