import airsim
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

async def move_drone():
    vehicle_name=select_drone()
    x = float(input("x-coordinate: "))
    y = float(input("y-coordinate: "))
    z = -float(input("z-coordinate: "))
    
    client.moveToPositionAsync(x=x, y=y, z=z, velocity=5.0, vehicle_name=vehicle_name)


def addDrone():
    droneName = input("New drone name: ")
    for drone in client.listVehicles():
        if drone == droneName:
            return 0
        
    x = float(input("x-coordinate: "))
    y = float(input("y-coordinate: "))
    z = -float(input("z-coordinate: "))
    
    pose = airsim.Pose(airsim.Vector3r(x_val=x, y_val=y, z_val=z), airsim.to_quaternion(0, 0, 0))
    client.simAddVehicle(vehicle_name=droneName, vehicle_type="simpleflight", pose=pose)
    client.enableApiControl(is_enabled=True, vehicle_name=droneName)
    client.armDisarm(arm=True, vehicle_name=droneName)
    client.takeoffAsync(timeout_sec=10.0, vehicle_name=droneName)

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
async def game():
    init()
    while True:
        str = input('Please enter the command(quit/takeoff/landing/move/add/show): ')
        if str == 'quit':
            break
        elif str == 'takeoff':
            takeoff()
        elif str =='move':
            await move_drone()
        elif str == 'landing':
            landing()
        elif str == 'add':
            addDrone()
        elif str =='show':
            show_pos(select_drone())
        else:
            pass

asyncio.run(game())
print('Program quit')