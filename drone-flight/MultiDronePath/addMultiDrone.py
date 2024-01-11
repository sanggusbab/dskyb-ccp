import airsim

# AirSim 연결
client = airsim.MultirotorClient()
client.confirmConnection()

#드론 초기 위치 지정
pose = airsim.Pose(airsim.Vector3r(x_val=3, y_val=3, z_val=0), airsim.to_quaternion(0, 0, 0))

# 드론 추가 및 제어

for i in range(3):
    
    client.simAddVehicle("MyDrone" + str(i), "simpleflight", pose)
    client.enableApiControl(True, vehicle_name="MyDrone"+str(i))
    client.armDisarm(True, vehicle_name="MyDrone"+str(i))
    client.takeoffAsync(timeout_sec=10.0, vehicle_name="MyDrone"+str(i))
    client.moveToPositionAsync(x=50+i*20, y=50+i*10, z=0, velocity=5.0, vehicle_name="MyDrone"+str(i))
    
    print(client.listVehicles())


