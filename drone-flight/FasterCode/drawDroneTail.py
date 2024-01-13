import time
import pygame
import os
import sys
import json
import math

current_script_path = os.path.abspath(__file__)
upper_folder_path = os.path.dirname(os.path.dirname(current_script_path))
sys.path.append(upper_folder_path)
import airsim
from collections import deque

def update_drone_position(drone_positions, x_center, y_center, pose, vehicle_name):
    drone_positions[vehicle_name]["positions"].append((x_center + pose.position.x_val, y_center + pose.position.y_val))

def drawLine(drone_positions, background, resized_image, map_image):
    background.blit(map_image, (0, 0))
    for vehicle_name, data in drone_positions.items():
        positions = data["positions"]
        background.blit(resized_image, [positions[-1][0], positions[-1][1]])
        for i in range(len(positions) - 1):
            new_color = data["TailColor"][i]
            pygame.draw.line(background, new_color, positions[i], positions[i+1], 3)

def main():
    client = airsim.MultirotorClient()
    client.confirmConnection()
    pygame.init()
    original_image = pygame.image.load("drone.png")
    map_image = pygame.image.load("map.png")
    resized_image = pygame.transform.scale(original_image, (20, 14))
    drone_positions = {}
    background = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('PYGAME_2')
    x_center = background.get_size()[0] // 2 -10
    y_center = background.get_size()[1] // 2 -7
    background.blit(map_image, (0, 0))
    count = 0
    drone = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[]}
    subgroup = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    TailColor = [
        [(255,230,230), (255,180,180), (255,130,130), (255,80,80),  (255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0)],
        [(230,255,230), (180,255,180), (130,255,130), (80,255,80),  (0,255,0),(0,255,0),(0,255,0),(0,255,0),(0,255,0),(0,255,0)],
        [(230,230,255), (180,180,255), (130,130,255), (80,80,255),  (0,0,255),(0,0,255),(0,0,255),(0,0,255),(0,0,255),(0,0,255)],
        [(255,255,230), (255,255,180), (255,255,130), (255,255,80), (255,255,0),(255,255,0),(255,255,0),(255,255,0),(255,255,0),(255,255,0)],
        [(255,230,255), (255,180,255), (255,130,255), (255,80,255), (255,0,255),(255,0,255),(255,0,255),(255,0,255),(255,0,255),(255,0,255)],
        [(230,255,255), (180,255,255), (130,255,255), (80,255,255), (0,255,255),(0,255,255),(0,255,255),(0,255,255),(0,255,255),(0,255,255)],
        [(230,230,230), (180,180,180), (130,130,130), (80,80,80),   (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
        [(150,130,130), (150,100,100), (150,70,70), (150,40,40),    (150,0,0),(150,0,0),(150,0,0),(150,0,0),(150,0,0),(150,0,0)],
        [(130,150,130), (100,150,100), (70,150,70), (40,150,40),    (0,150,0),(0,150,0),(0,150,0),(0,150,0),(0,150,0),(0,150,0)],
        [(130,130,150), (100,100,150), (70,70,150), (40,40,150),    (0,0,150),(0,0,150),(0,0,150),(0,0,150),(0,0,150),(0,0,150)],
        [(150,150,130), (150,150,100), (150,150,70), (150,150,40),  (150,150,0),(150,150,0),(150,150,0),(150,150,0),(150,150,0),(150,150,0)],
        [(150,130,150), (150,100,150), (150,70,150), (150,40,150),  (150,0,150),(150,0,150),(150,0,150),(150,0,150),(150,0,150),(150,0,150)],
        [(130,150,150), (100,150,150), (70,150,150), (40,150,150),  (0,150,150),(0,150,150),(0,150,150),(0,150,150),(0,150,150),(0,150,150)],
        [(200,200,200), (200,170,170), (200,150,150), (200,130,130), (200,100,100), (200,100,100), (200,100,100), (200,100,100), (200,100,100), (200,100,100)],
        [(200,200,200), (170,170,200), (150,150,200), (130,130,200), (100,100,200), (100,100,200), (100,100,200), (100,100,200), (100,100,200), (100,100,200)],
    ]
    for i, vehicle_name in enumerate(client.listVehicles()):
        drone_positions[vehicle_name] = {"positions": deque(maxlen=10), "TailColor": TailColor[i]}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               return
        for vehicle_name in client.listVehicles():
            pose = client.simGetVehiclePose(vehicle_name=vehicle_name)
            update_drone_position(drone_positions, x_center, y_center, pose, vehicle_name)
            if (count%3) == 1:
                i = int(vehicle_name.replace('Drone', ''))
                if subgroup[i-1] == 0:
                    sorted_locations = sorted(drone[i], key=lambda loc: math.sqrt((int(loc[0])-400 - pose.position.x_val)**2 + (int(loc[1])-400 - pose.position.y_val)**2))
                    if len(sorted_locations)>0:
                        closest_location = sorted_locations[0]
                        distance_to_closest_location = math.sqrt((int(closest_location[0]) - 400 - pose.position.x_val)**2 + (int(closest_location[1]) - 400 - pose.position.y_val)**2)
                        client.moveToPositionAsync(x=int(closest_location[0])-400, y=int(closest_location[1])-400, z=-50, velocity=40.0, vehicle_name=vehicle_name)
                        if distance_to_closest_location <=4:
                            subgroup[i-1] = 1
                else:
                    distance_to_closest_location = math.sqrt((int(closest_location[2]) - 400 - pose.position.x_val)**2 + (int(closest_location[3]) - 400 - pose.position.y_val)**2)
                    if distance_to_closest_location <=4:
                        subgroup[i-1] = 0
                        if len(drone[i]) >0:
                            drone[i].pop(0)
                    if len(sorted_locations)>0:
                        client.moveToPositionAsync(x=int(closest_location[2]-400), y=int(closest_location[3])-400, z=-50, velocity=40.0, vehicle_name=vehicle_name)
                    else:
                        subgroup[i-1] = 0
                        if len(drone[i]) >0:
                            drone[i].pop(0)
        drawLine(drone_positions, background, resized_image, map_image)
        if (count%3) == 0:
            try:
                with open('../data.json', 'r') as existing_file:
                    existing_data  = json.load(existing_file)
                    seen_locations  = set()
                    filtered_data = []
                    for entry in existing_data :
                        locations = (entry["Location1_x"],
                                     entry["Location1_y"],
                                     entry["Location2_x"],
                                     entry["Location2_y"])
                        if locations not in seen_locations:
                            filtered_data.append(entry)
                            seen_locations.add(locations)
            except (FileNotFoundError, json.JSONDecodeError):
                filtered_data = []
            with open('../data.json', 'w') as json_file:
                json.dump([], json_file, indent=2)
            for entry in filtered_data:
                drone[int(entry["device_id"])].append([value for key, value in entry.items() if key != 'device_id'])
            count = count + 1
        else:
            count = count + 1
        pygame.display.update()
        time.sleep(2)
     
if __name__ == "__main__":
    main()