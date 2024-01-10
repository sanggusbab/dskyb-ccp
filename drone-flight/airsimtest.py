import airsim
import numpy as np
import os
import pprint
from setuptools import setup
import tempfile
import sys
import time
import threading

sys.path.append(os.path.join(os.path.abspath(os.path.split(__file__)[0])))

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

#obstacle detection


def check_stop_key():
    while True:
        stop = input("Press 's' to stop moving: ")
        if stop == 's':
            client.hoverAsync().join()
            break
time.sleep(0.1)

def move_drone():
    x = float(input("x-coordinate of the destination (forward is positive): "))
    y = float(input("y-coordinate of the destination (right is positive): "))
    z = -float(input("z-coordinate of the destination (upward is positive): "))
    
    stop_thread = threading.Thread(target=check_stop_key)
    stop_thread.start()
    
    client.moveToPositionAsync(x, y, z, 5).join()

    #images = get_drone_images()
    
    #if detect_obstacles(images):
        #print("Obstacle detected!")
        #avoid_obstacles()
    stop_thread.join()

def game():
    while True:        
        str = input('Please enter the command: ')
        if str == 'quit':
            break

        elif str == 'takeoff':
            client.takeoffAsync().join()
            move = input('Move or not?')
            if move.lower() in ['m', 'y']:
                move_drone()
                time.sleep(0.1)
                initializing_part()
                
        elif str == 'landing':
            print("Landing...")
            client.landAsync().join()

    print('Game finished')

def initializing_part():
    pose = client.simGetVehiclePose()
    print("Drone's current position:")
    print("x: ", pose.position.x_val)
    print("y: ", pose.position.y_val)
    print("z: ", pose.position.z_val)
    
    cntr = input('Do you want to start program?: s, y: start || q, n: quit)')
    return cntr

while True:
    cntr = initializing_part()
    if cntr.lower() in ['s', 'y']:
        game()
    elif cntr.lower() in ['q', 'n']:
        break
    else:
        pass

print()
client.armDisarm(False)
client.enableApiControl(False)
print('Program quit')
