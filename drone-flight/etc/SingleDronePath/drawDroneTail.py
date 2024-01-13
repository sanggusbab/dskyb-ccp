import time
import pygame
from collections import deque
pygame.init()  

background = pygame.display.set_mode((960, 720))   
pygame.display.set_caption('PYGAME_2')

x_center = background.get_size()[0]//2
y_center = background.get_size()[1]//2

drone_positions = deque(maxlen=20)
def extract_coordinates_from_string(file_path):
 while True:
    try: 
      with open(file_path, 'r') as file:
        line = file.readline()
        coordinates_str = line.split(":")[1].strip()
        x_str, y_str= coordinates_str.split(",")
        x = float(x_str.strip())
        y = float(y_str.strip())
        print("x_position: ", x)
        print("y_position: ", y)
        drone_positions.append((x_center+x,y_center+y))
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            play = False
        background.fill((255,255,255))
        pygame.draw.circle(background, (255,0,0), (x_center+x,y_center+y), 5, 5)
        if len(drone_positions) >= 2:
              for i in range(len(drone_positions) - 1):
                color_intensity = 230-i*10
                color = (color_intensity, color_intensity, 255)
                pygame.draw.line(background, color, drone_positions[i], drone_positions[i+1], 7)
        else:
          print("Not enough points to draw lines.")
        pygame.draw.line(background, (0,0,0), (x_center,0), (x_center,y_center*2))
        pygame.draw.line(background, (0,0,0), (0,y_center), (x_center*2,y_center))
        pygame.display.update()
        time.sleep(1)
    except FileNotFoundError:
      print(f"File not found: {file_path}")
      break

output_file_path = "../DronePosition.txt"
extract_coordinates_from_string(output_file_path)

pygame.quit()

