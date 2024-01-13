import time
import pygame
import airsim
from collections import deque

client = airsim.MultirotorClient()
client.confirmConnection()

pygame.init() 

# define constant
MAX_POSITIONS = 5
DRONE_LIMIT = 15
NEW_WIDTH, NEW_HEIGHT = 40, 40
IMAGE_PATH = "drone.png"

#initialize
drone_positions = {}
count =0

#set pygame background
background = pygame.display.set_mode((960, 720))
pygame.display.set_caption('PYGAME_2')
x_center = background.get_size()[0] // 2
y_center = background.get_size()[1] // 2
background.fill((255, 255, 255))
pygame.draw.line(background, (0, 0, 0), (x_center, 0), (x_center, y_center * 2))
pygame.draw.line(background, (0, 0, 0), (0, y_center), (x_center * 2, y_center))

# image
original_image = pygame.image.load(IMAGE_PATH)
image_rect = original_image.get_rect()
resized_image = pygame.transform.scale(original_image, (NEW_WIDTH, NEW_HEIGHT))


TailColor = [
    [(255,230,230), (255,180,180), (255,130,130), (255,80,80), (255,0,0)],
    [(230,255,230), (180,255,180), (130,255,130), (80,255,80), (0,255,0)],
    [(230,230,255), (180,180,255), (130,130,255), (80,80,255), (0,0,255)],
    [(255,255,230), (255,255,180), (255,255,130), (255,255,80), (255,255,0)],
    [(255,230,255), (255,180,255), (255,130,255), (255,80,255), (255,0,255)],
    [(230,255,255), (180,255,255), (130,255,255), (80,255,255), (0,255,255)],
    [(230,230,230), (180,180,180), (130,130,130), (80,80,80), (0,0,0)],
    [(150,130,130), (150,100,100), (150,70,70), (150,40,40), (150,0,0)],
    [(130,150,130), (100,150,100), (70,150,70), (40,150,40), (0,150,0)],
    [(130,130,150), (100,100,150), (70,70,150), (40,40,150), (0,0,150)],
    [(150,150,130), (150,150,100), (150,150,70), (150,150,40), (150,150,0)],
    [(150,130,150), (150,100,150), (150,70,150), (150,40,150), (150,0,150)],
    [(130,150,150), (100,150,150), (70,150,150), (40,150,150), (0,150,150)],
    [(200,200,200), (200,170,170), (200,150,150), (200,130,130), (200,100,100)],
    [(200,200,200), (170,170,200), (150,150,200), (130,130,200), (100,100,200)]
]



def update_drone_position(vehicle_name):
        global count
        pose = client.simGetVehiclePose(vehicle_name=vehicle_name)

        if count<15:
             if vehicle_name not in drone_positions:
                    drone_positions[vehicle_name] = {"positions": deque(maxlen=MAX_POSITIONS), "TailColor": TailColor[count]}
                    count= count +1
        else:
            print(f"Failed to get {vehicle_name}'s position.")
        drone_positions[vehicle_name]["positions"].append((x_center + pose.position.x_val, y_center + pose.position.y_val))
        


def drawLine():
    background.fill((255, 255, 255))

    for vehicle_name, data in drone_positions.items():
        positions = data["positions"]
        current_position = positions[-1]
        background.blit(resized_image, current_position)

        if len(positions) >= 2:
            for i in range(len(positions) - 1):
                new_color = data["TailColor"][i]
                pygame.draw.line(background, new_color, positions[i], positions[i+1], 7)     
        else:
            print("Not enough points to draw lines.")
    pygame.draw.line(background, (0, 0, 0), (x_center, 0), (x_center, y_center * 2))
    pygame.draw.line(background, (0, 0, 0), (0, y_center), (x_center * 2, y_center))
    pygame.display.update()        

def main():
    pygame.display.update()
    num =0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               return drone_positions
            
        for vehicle_name in client.listVehicles():
            update_drone_position(vehicle_name)    
        
        num = num+1
        time.sleep(1)

        if num >4:  #after 5 seconds
            drawLine()
            num =0
     
if __name__ == "__main__":
    main()
