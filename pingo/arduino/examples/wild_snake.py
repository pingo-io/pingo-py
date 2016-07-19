
"""

Snake head position and direction is coded like pictured below, i.e. when
the snake head is at the middle segment going right, the code is 6, going left
in the same place the code is 13.

      >:0
      <:7
      ----
^:5  |    | v:1
v:12 |>:6 | ^:8
      ----
^:4  |<:13| v:2
v:11 |    | ^:9
      ----
      <:3
      >:10

To understand this diagram, read:

> as a right arrow
< as a left arrow
v as a down arrow
^ as an up arrow
"""

from time import sleep
from random import choice

import pingo

ard = pingo.arduino.get_arduino()

#           A   B  C  D  E  F   G
display = [12, 13, 7, 8, 9, 11, 10]

pins = [ard.pins[p] for p in display]

# move choices are ordered with the following logic:
# (1) when both choices are turns, right turn is first;
# (2) when one choice is a turn and the other is straight, turn is first
moves = {
    0: [1],
    1: [13, 2],
    2: [3],
    3: [4],
    4: [6, 5],
    5: [0],
    6: [2, 8],
    7: [12],
    8: [7],
    9: [13, 8],
    10: [9],
    11: [10],
    12: [6, 11],
    13: [5, 11]
}

for pin in pins:
    pin.mode = pingo.OUT

head = 0  # code 0 -> top segment, going left
tail = 5

pot = ard.pins['A0']

while True:
    pins[head % 7].high()
    sleep(pot.ratio())
    pins[tail % 7].low()
    tail = head
    next = moves[head]
    head = choice(next)
