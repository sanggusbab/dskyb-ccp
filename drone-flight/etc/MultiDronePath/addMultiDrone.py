import sys
import os
current_script_path = os.path.abspath(__file__)
upper_folder_path = os.path.dirname(os.path.dirname(current_script_path))
sys.path.append(upper_folder_path)
import airsim
import time
client = airsim.MultirotorClient()
client.confirmConnection()

pose = airsim.Pose(airsim.Vector3r(x_val=3, y_val=3, z_val=0), airsim.to_quaternion(0, 0, 0))

for i in range(3):
    
    client.simAddVehicle("MyDrone" + str(i), "simpleflight", pose)
    client.enableApiControl(True, vehicle_name="MyDrone"+str(i))
    client.armDisarm(True, vehicle_name="MyDrone"+str(i))
    client.takeoffAsync(timeout_sec=10.0, vehicle_name="MyDrone"+str(i))
    client.moveToPositionAsync(x=50+i*20, y=50+i*10, z=0, velocity=5.0, vehicle_name="MyDrone"+str(i))
    
    print(client.listVehicles())


