import urx
import time


#Settings and parameters
rob = urx.Robot("10.42.0.35")
rob.set_tcp((0, 0, 0.1, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
time.sleep(1)  #leave some time to robot to process the setup commands


l = 0.05
v = 0.05 #velocit
a = 0.3 #acceleration

rob.movej((0.5, 0, 0, 0, 0, 0), a, v, relative=True) #functions the same as in urscript

#print("Current location is:", rob.getl())

#rob.movel((0.1, 0, 0, 0, 0, 0), a, v, relative=true)

rob.stopl()
