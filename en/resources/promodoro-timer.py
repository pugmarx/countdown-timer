#!/bin/python3

from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep

sense = SenseHat()

sense.set_rotation(90)
sense.low_light = True

SLEEP_SEC = 23.4375
#SLEEP_SEC = .5

MAX_RANGE=64
#MAX_RANGE=10

G = [0, 255, 100]  # green
R = [255, 100, 0] # red
X = [0, 0, 0]  # off

secs = 1500
#timer = [ G for i in range(secs)] + [ X for j in range(64 - secs) ]

while True:
  global i
  sense.clear()
  timer = [X for j in range(64)]

  sense.set_pixels(timer)


  # 1500 second timer
  for i in range(0, MAX_RANGE):
  
    global flag
    flag = False
    print("i = {}".format(i))  
    sleep(SLEEP_SEC)
    timer[i] = R
    sense.set_pixels(timer)
    while True:
      for event in sense.stick.get_events():
          print("The joystick was {} {}".format(event.action, event.direction))
          if event.action == ACTION_RELEASED:
              flag = True
              sense.clear()
      break
   
    
    #print("flag {}".format(flag))
    if flag == True:
      i = 0
      break
    #if i < 63:
    #   break

  for i in range(0, 3):
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
    sleep(0.1)
