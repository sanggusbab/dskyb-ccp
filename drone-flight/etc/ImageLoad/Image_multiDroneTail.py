
import time
import pygame
import sys
from collections import deque

pygame.init()  
background = pygame.display.set_mode((960, 720))
pygame.display.set_caption('PYGAME_2')

x_center = background.get_size()[0] // 2
y_center = background.get_size()[1] // 2

image_path = "drone.png"
original_image = pygame.image.load(image_path)
image_rect = original_image.get_rect()

new_width, new_height = 40, 40
resized_image = pygame.transform.scale(original_image, (new_width, new_height))

def extract_coordinates_from_string(file_path):
    
    drone_positions = {}
    max_positions = 20
    count = 0
    color_intensity = 0 
    
    while True:
        try: 
            with open(file_path, 'r') as file:
                for line in file:
                    vehicle_name = line.split(" ")[0]
                    coordinates_str = line.split(":")[1].strip()
                    x_str, y_str = coordinates_str.split(",")
                    x = float(x_str.strip())
                    y = float(y_str.strip())
                    print(f"{vehicle_name} - x_position: {x}, y_position: {y}")
                    color = [
                        (255,color_intensity, color_intensity),
                        (color_intensity, 255, color_intensity),
                        (color_intensity, color_intensity, 255),
                        (255, 255, color_intensity),
                        (255, color_intensity, 255),
                        (color_intensity, 255, 255),
                        (color_intensity, color_intensity, color_intensity),
                        (255,color_intensity, color_intensity),
                        (color_intensity, 255, color_intensity),
                        (color_intensity, color_intensity, 255),
                        (255, 255, color_intensity),
                        (255, color_intensity, 255),
                        (color_intensity, 255, 255),
                        (color_intensity, color_intensity, color_intensity),
                        (255,color_intensity, color_intensity),
                        (color_intensity, 255, color_intensity),
                        (color_intensity, color_intensity, 255),
                        (255, 255, color_intensity),
                        (255, color_intensity, 255),
                        (color_intensity, 255, 255),
                        (color_intensity, color_intensity, color_intensity)
                    ]
                    if vehicle_name not in drone_positions:
                        drone_positions[vehicle_name] = {"color": color[count], "positions": deque(maxlen=max_positions)}
                        count= count +1
                        print(drone_positions[vehicle_name]["color"])
                    drone_positions[vehicle_name]["positions"].append((x_center + x, y_center + y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return drone_positions
            background.fill((255, 255, 255))

            for vehicle_name, data in drone_positions.items():
                positions = data["positions"]
                
                if len(positions) >= 2:
                    for i in range(len(positions) - 1):
                        color_intensity = 230-i*10 
                        print(f"color_indensity: {color_intensity}")
                        data["color_list"] = list(data["color"])
                        if data["color_list"][0] != 255:
                          data["color_list"][0] = color_intensity
                        if data["color_list"][1] != 255:
                          data["color_list"][1] = color_intensity
                        if data["color_list"][2] != 255:
                          data["color_list"][2] = color_intensity
                        new_color = tuple(data["color_list"])
                        pygame.draw.line(background, new_color, positions[i], positions[i+1], 7)
                        print(data["color"])
                        print(new_color)
                else:
                    print("Not enough points to draw lines.")
            for vehicle_name, data in drone_positions.items():
                current_position = data["positions"][-1]
                background.blit(resized_image, current_position)
            pygame.draw.line(background, (0, 0, 0), (x_center, 0), (x_center, y_center * 2))
            pygame.draw.line(background, (0, 0, 0), (0, y_center), (x_center * 2, y_center))
            pygame.display.update()
            time.sleep(1)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            break

def main():
    output_file_path = "../DronePositions.txt"
    while True:
        extract_coordinates_from_string(output_file_path)

if __name__ == "__main__":
    main()
