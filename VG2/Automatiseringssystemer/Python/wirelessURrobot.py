import pygame
import urx
import time

#Reference for robot
rob = urx.Robot("10.42.0.35")

rob.set_tcp((0, 0, 0.1, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
time.sleep(0.2)  #leave some time to robot to process the setup commands

def move_rob(keys):
    speed = 0.5  #Reference speed

    if keys[pygame.K_UP]:
        rob.translate((0, 0, speed, 0, 0, 0), acc=0.5, vel=0.1) #Move the UR robot by "speed" in the z axis if UP is pressed
        print("Up")
    elif keys[pygame.K_DOWN]:
        rob.translate((0, 0, -speed, 0, 0, 0), acc=0.5, vel=0.1)
        print("Down")
    elif keys[pygame.K_LEFT]:
        rob.translate((0, -speed, 0, 0, 0, 0), acc=0.5, vel=0.1)
        print("Left")
    elif keys[pygame.K_RIGHT]:
        rob.translate((0, speed, 0, 0, 0, 0), acc=0.5, vel=0.1)
        print("Right")

# Initialize pygame
pygame.init()

#Make a small pygame window
pygame.display.set_mode((640, 480))

while True:
    #if pygame quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the rob based on key input
    move_rob(keys)

#Close connection to robot when program ends
rob.close()