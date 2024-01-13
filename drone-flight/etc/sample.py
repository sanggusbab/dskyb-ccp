import airsim
from setuptools import setup
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
circle_radius = 300
num_drones = 14

time.sleep(5)
for i in range(len(droneList)):
    droneName = f"Drone{i+1}"
    client.enableApiControl(is_enabled=True, vehicle_name=droneName)

for i in range(len(droneList)):
    angle_deg = i * (360 / num_drones)
    x, y = calculate_circle_position(circle_radius, angle_deg)
    droneName = f"Drone{i+1}"
    client.takeoffAsync(timeout_sec=1,vehicle_name=droneName)
    pose = client.simGetVehiclePose(vehicle_name=droneName)
    client.moveToPositionAsync(x=pose.position.x_val, y=pose.position.y_val, z=-80, velocity=30.0, vehicle_name=droneName)

time.sleep(10)
while True:
    for i in range(len(droneList)):
        angle_deg = i * (360 / num_drones)
        x, y = calculate_circle_position(circle_radius, angle_deg)
        droneName = f"Drone{i+1}"
        client.moveToPositionAsync(x=x, y=y, z=-80, velocity=60.0, vehicle_name=droneName)
    
    time.sleep(4)
    circle_radius = 100
    for i in range(len(droneList)):
        angle_deg = ((i+11)%14) * (360 / num_drones)
        x, y = calculate_circle_position(circle_radius, angle_deg)
        droneName = f"Drone{i+1}"
        client.moveToPositionAsync(x=x, y=y, z=-80, velocity=60.0, vehicle_name=droneName)
    
    time.sleep(4)
    circle_radius = 150
    for i in range(len(droneList)):
        angle_deg = ((i+7)%14) * (360 / num_drones)
        x, y = calculate_circle_position(circle_radius, angle_deg)
        droneName = f"Drone{i+1}"
        client.moveToPositionAsync(x=x, y=y, z=-80, velocity=60.0, vehicle_name=droneName)
    
    time.sleep(4)
    circle_radius = 200
    for i in range(len(droneList)):
        angle_deg = (i+3) * (360 / num_drones)
        x, y = calculate_circle_position(circle_radius, angle_deg)
        droneName = f"Drone{i+1}"
        client.moveToPositionAsync(x=x, y=y, z=-80, velocity=60.0, vehicle_name=droneName)
    
    time.sleep(4)
    circle_radius = 150
    for i in range(len(droneList)):
        angle_deg = (i+3) * (360 / num_drones)
        x, y = calculate_circle_position(circle_radius, angle_deg)
        droneName = f"Drone{i+1}"
        client.moveToPositionAsync(x=x, y=y, z=-80, velocity=60.0, vehicle_name=droneName)

    time.sleep(10)

