import airsim
import time

# 드론 위치 1초마다 파일에 저장

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()
client.moveToPositionAsync(80,70, -50, 5)

def update_drone_position(file_path):
      
 while True:
    pose = client.simGetVehiclePose()
    print("Drone's current position:")
    print("x: ", pose.position.x_val)
    print("y: ", pose.position.y_val)

    if pose:
            # 위치 정보를 파일에 업데이트
            with open(file_path, 'w') as file:
                file.write(f"Drone Position: {pose.position.x_val}, {pose.position.y_val}")

            # 1초 대기
            time.sleep(1)
    else:
            print("Failed to get drone position.")
            break
    
    time.sleep(1)

# 파일 경로 설정 
output_file_path = "C:/Users/dlwng/Downloads/DronePosition.txt"

update_drone_position(output_file_path)




