import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
client.takeoffAsync().join()
client.moveToPositionAsync(80,70, -50, 5)
def update_drone_position(file_path):
 while True:
    pose = client.simGetVehiclePose()
    print("Drone's current position:")
    print("x: ", pose.position.x_val)
    print("y: ", pose.position.y_val)
    if pose:
            with open(file_path, 'w') as file:
                file.write(f"Drone Position: {pose.position.x_val}, {pose.position.y_val}")
            time.sleep(1)
    else:
            print("Failed to get drone position.")
            break
    time.sleep(1)

output_file_path = "../DronePosition.txt"

update_drone_position(output_file_path)




