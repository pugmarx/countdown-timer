#!/bin/python3

from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep

sense = SenseHat()

sense.set_rotation(90)
sense.low_light = True



G = [0, 255, 100]  # green
R = [255, 100, 0] # red
X = [0, 0, 0]  # off

secs = 1500
#timer = [ G for i in range(secs)] + [ X for j in range(64 - secs) ]

while True:
  timer = [X for j in range(64)]

  sense.set_pixels(timer)

  global i

  # 1500 second timer
  for i in range(0, 64):
  
    print("i = {}".format(i))  
    #sleep(23.4375)
    sleep(1)
    timer[i] = R
    sense.set_pixels(timer)
    while True:
      for event in sense.stick.get_events():
          print("The joystick was {} {}".format(event.action, event.direction))
          if event.action == ACTION_RELEASED:
              i = 0
              sense.clear()
      break
  if i < 64:
      break

  for i in range(0, 64):
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
    sleep(0.1)
