import urx
import time


rob = urx.Robot("10.42.0.35")
rob.set_tcp((0, 0, 0.1, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
time.sleep(1)  #leave some time to robot to process the setup commands

l = 0.05
v = 0.05
a = 0.3

while True:
    Direction = input("What direction")
    if Direction == "UP":
        rob.movej((0, -0.2, 0, 0, 0, 0), a, v, relative=True)
        rob.stopj(a)
    time.sleep(0.5)
    
#rob.stopl()
