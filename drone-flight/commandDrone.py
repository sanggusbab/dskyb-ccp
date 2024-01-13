import json
import airsim
from setuptools import setup
import asyncio
import time
import math

def calculate_circle_position(radius, angle_deg):
    angle_rad = math.radians(angle_deg)
    x = radius * math.cos(angle_rad)
    y = radius * math.sin(angle_rad)
    return x, y

client = airsim.MultirotorClient()
client.confirmConnection()
droneList = client.listVehicles()
circle_radius = 10
num_drones = 15

for i in range(num_drones - len(droneList)):
    index = num_drones - len(droneList) - i
    angle_deg = index * (360 / num_drones)
    x, y = calculate_circle_position(circle_radius, angle_deg)
    pose = airsim.Pose(airsim.Vector3r(x_val=0, y_val=0, z_val=0), airsim.to_quaternion(0, 0, 0))
    droneName = f"Drone{index}"
    client.simAddVehicle(vehicle_name=droneName, vehicle_type="simpleflight", pose=pose)
    client.enableApiControl(is_enabled=True, vehicle_name=droneName)
    client.takeoffAsync(timeout_sec=1.0,vehicle_name=droneName)
    client.moveToPositionAsync(x=x, y=y, z=-10, velocity=10.0, vehicle_name=droneName)
    pose = client.simGetVehiclePose(vehicle_name=droneName)
    print(f"Drone {num_drones - i}'s current position:")
    time.sleep(1)
    print("x: ", pose.position.x_val)
    print("y: ", pose.position.y_val)
    print("z: ", pose.position.z_val)

droneList = client.listVehicles()

with open("./data.json", 'r') as file:
    json_data = json.load(file)

filtered_data = [item for item in json_data if not (item.get('key') != 'value')]

with open("./data.json", 'w') as file:
    json.dump(filtered_data, file, indent=2)