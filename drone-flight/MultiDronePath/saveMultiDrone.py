import airsim
import time

# AirSim 연결
client = airsim.MultirotorClient()
client.confirmConnection()


def update_drone_position(vehicle_name, file_path):
        pose = client.simGetVehiclePose(vehicle_name=vehicle_name)
        print(f"{vehicle_name}'s current position:")
        print("x: ", pose.position.x_val)
        print("y: ", pose.position.y_val)

        if pose:
            # 위치 정보를 파일에 업데이트
            with open(file_path, 'a') as file:
                file.write(f"{vehicle_name} Position: {pose.position.x_val}, {pose.position.y_val}\n")
        else:
            print(f"Failed to get {vehicle_name}'s position.")
        



def main():
    output_file_path = "C:/Users/dlwng/Downloads/DronePositions.txt"


    # 모든 드론들의 위치를 파일에 업데이트
    while True:
        for vehicle_name in client.listVehicles():
            update_drone_position(vehicle_name, output_file_path)

        #1초대기
        time.sleep(1)

        with open(output_file_path, 'w') as file:
            file.write("")  # 파일 내용을 비워줌 (5개의 드론의 위치만 남기고자함)
            
            

if __name__ == "__main__":
    main()
