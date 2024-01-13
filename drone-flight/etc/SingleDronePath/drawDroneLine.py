import time
import pygame

pygame.init()  
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('PYGAME_2')

x_center = background.get_size()[0]//2
y_center = background.get_size()[1]//2

def extract_coordinates_from_string(file_path):

 drone_positions = []

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
        drone_positions.append((240+x,180+y))

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            play = False
        background.fill((255,255,255))
        pygame.draw.circle(background, (255,0,0), (240+x,180+y), 5, 5)
        if len(drone_positions) >= 2:
          pygame.draw.lines(background, (0, 0, 255), False, drone_positions, 2)
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

