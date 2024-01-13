import airsim
import numpy as np
import os
import pprint
from setuptools import setup
import asyncio

client = airsim.MultirotorClient()
client.confirmConnection()

#dlrj cnrkgka
def init():
    dname = client.listVehicles()
    for drone in dname:
        client.enableApiControl(is_enabled=True, vehicle_name=drone)
        client.armDisarm(arm=True, vehicle_name=drone)
        

def select_drone():
    droneList = client.listVehicles()
    idx = 0
    for drone in droneList:
        print(f'{idx}th drone: {drone}')
        idx = idx +1
    while True:
        try:
            drone_index = int(input("Choose a drone:"))
            if 0 <= drone_index < len(droneList):
                drone = droneList[drone_index]
                print(drone)
                return drone
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_pos(vehicle_name):
    pose = client.simGetVehiclePose(vehicle_name)
    print("Drone's current position:")
    print("x: ", pose.position.x_val)
    print("y: ", pose.position.y_val)
    print("z: ", pose.position.z_val)       

def start_program():
    start = input('Do you want to start program?: start)')
    if start == 'start':
        game()

#delete
async def check_stop_key(vehicle_name):
    while True:
        stop = input("Press 's' to stop moving: ")
        if stop == 's':
            client.hoverAsync(vehicle_name=vehicle_name)
            break

def addDrone():
    droneName = input("New drone name: ")
    for drone in client.listVehicles():
        if drone == droneName:
            return 0
        
    x = float(input("x-coordinate: "))
    y = float(input("y-coordinate: "))
    z = 0
    #-float(input("z-coordinate: "))
    
    pose = airsim.Pose(airsim.Vector3r(x_val=x, y_val=y, z_val=0), airsim.to_quaternion(0, 0, 0))
    client.simAddVehicle(vehicle_name=droneName, vehicle_type="simpleflight", pose=pose)
    client.enableApiControl(is_enabled=True, vehicle_name=droneName)
    client.armDisarm(arm=True, vehicle_name=droneName)
    #client.takeoffAsync(timeout_sec=10.0, vehicle_name=droneName)
    
def deleteDrone():
    vehicle_name = select_drone()
    client.simRemoveVehicle(vehicle_name)
    print(f'{vehicle_name} has been removed.')
    

async def move_drone():
    vehicle_name=select_drone()
    x = float(input("x-coordinate: "))
    y = float(input("y-coordinate: "))
    z = -float(input("z-coordinate: "))
    
    client.moveToPositionAsync(x=x, y=y, z=z, velocity=5.0, vehicle_name=vehicle_name)

def takeoff():
    print("TAKEOFF MODE")
    client.takeoffAsync(10.0, select_drone())

def landing():
    vehicle_name = select_drone()
    landed = client.getMultirotorState(vehicle_name=vehicle_name).landed_state
    if landed == airsim.LandedState.Landed:
        print("already landed...")
    else:
        print("landing...")
        client.landAsync(vehicle_name=vehicle_name)
        
async def get_positions(drones):
    positions = []
    for drone in drones:
        pose = client.simGetVehiclePose(drone)
        positions.append(((pose.position.x_val, pose.position.y_val, pose.position.z_val), drone))
    return positions

async def check_collision(positions):
    client.simGetCollisionInfo
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            if abs(positions[i][0][0] - positions[j][0][0]) <= 1 and abs(positions[i][0][1] - positions[j][0][1]) <= 1 and abs(positions[i][0][2] - positions[j][0][2]) <= 1:
                print("Collision!")
                # if collision --> right +1
                client.moveByVelocityAsync(1, 0, 0, 1, vehicle_name=positions[i][1])
                return
    await asyncio.sleep(1)
    positions = await get_positions(client.listVehicles())
    check_collision(positions)
                                                   
async def game():
    init()
    while True:
  
        str = input('Please enter the command(quit/takeoff/landing/move/add/show): ')
        if str == 'quit':
            drones = client.listVehicles()
            num = 0
            for drone in drones:
                for num in range(len(drones)):
                    client.landAsync(vehicle_name=drones[num])
            break
        elif str == 'takeoff':
            takeoff()
        elif str =='move':
            await move_drone()
            #ask = input('multiple destination(yes/no)? : ')
            #if ask = yes
            #await move
        elif str == 'landing':
            landing()
        elif str == 'add':
            addDrone()
        elif str =='show':
            show_pos(select_drone())
        elif str == 'delete':
            deleteDrone()
        else:
            pass
        
        drones = client.listVehicles()
        positions = await get_positions(drones)
        await check_collision(positions)

asyncio.run(game())
print('Program quit')