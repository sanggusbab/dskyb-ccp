import sys
import os
current_script_path = os.path.abspath(__file__)
upper_folder_path = os.path.dirname(os.path.dirname(current_script_path))
sys.path.append(upper_folder_path)
import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()

def update_drone_position(vehicle_name, file_path):
        pose = client.simGetVehiclePose(vehicle_name=vehicle_name)
        print(f"{vehicle_name}'s current position:")
        print("x: ", pose.position.x_val)
        print("y: ", pose.position.y_val)
        if pose:
            with open(file_path, 'a') as file:
                file.write(f"{vehicle_name} Position: {pose.position.x_val}, {pose.position.y_val}\n")
        else:
            print(f"Failed to get {vehicle_name}'s position.")

def main():
    output_file_path = "../DronePositions.txt"
    while True:
        for vehicle_name in client.listVehicles():
            update_drone_position(vehicle_name, output_file_path)
        time.sleep(1)
        with open(output_file_path, 'w') as file:
            file.write("")

if __name__ == "__main__":
    main()
