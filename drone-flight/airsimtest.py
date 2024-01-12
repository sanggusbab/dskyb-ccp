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
def check_collision():
    collision_info = client.simGetCollisionInfo()
    if collision_info.has_collided:
        print("Drone has collided at position: ", collision_info.position)
        return True
    else:
        return False


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
    time.sleep(0.5)
    
    #if check_collision():
       # print("Collided")

    #images = get_drone_images()
    
    #if detect_obstacles(images):
        #print("Obstacle detected!")
        #avoid_obstacles()
    pose = client.simGetVehiclePose()
    print("Drone's current position:")
    print("x: ", pose.position.x_val)
    print("y: ", pose.position.y_val)
    print("z: ", pose.position.z_val)          

    land = input("Do you want to land? (y/n): ")
    if land.lower() == 'y':
        print("Landing...")
        client.landAsync().join()

    stop_thread.join()

def initializing_part():
    pose = client.simGetObjectPose('SimpleFlight')
    print("Drone's current position:")
    print("x: ", pose.position.x_val)
    print("y: ", pose.position.y_val)
    print("z: ", pose.position.z_val)
    
    cntr = input('Do you want to start program?: s, y: start || q, n: quit)')
    return cntr    

def start_program():
    start = input('Do you want to start program?: s, y: start || q, n: quit)')
    if start.lower() in ['s', 'y']:
        game()
    elif start.lower() in ['q', 'n']:
        print('Quitting program')
        return False

def game():
    while True:        
        str = input('Please enter the command(quit/takeoff/landing): ')
        if str == 'quit':
            print("QUIT")
            client.hoverAsync().join()
            print("Disconnecting...")
            client.armDisarm(False)
            client.enableApiControl(False)
            return False

        elif str == 'takeoff':
            client.takeoffAsync().join()
            move = input('Move or not?')
            if move.lower() in ['m', 'y']:
                move_drone()
                initializing_part()
                time.sleep(0.1)
                
        elif str == 'landing':
            print("Landing...")
            client.landAsync().join()
            pose = client.simGetVehiclePose()
            print("Drone's current position:")
            print("x: ", pose.position.x_val)
            print("y: ", pose.position.y_val)
            print("z: ", pose.position.z_val)             
            return False
        

while True:
    cntr = initializing_part()
    if cntr.lower() in ['s', 'y']:
        if game() is False: # add this line
            break # add this line
    elif cntr.lower() in ['q', 'n']:
        break
    else:
        pass


client.armDisarm(False)
client.enableApiControl(False)
print('Program quit')
