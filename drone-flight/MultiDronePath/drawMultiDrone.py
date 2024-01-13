import sys
import os
current_script_path = os.path.abspath(__file__)
upper_folder_path = os.path.dirname(os.path.dirname(current_script_path))
sys.path.append(upper_folder_path)
import airsim
import time
import pygame
import hashlib

pygame.init()  

background = pygame.display.set_mode((960, 720))
pygame.display.set_caption('PYGAME_2')

x_center = background.get_size()[0] // 2
y_center = background.get_size()[1] // 2


def extract_coordinates_from_string(file_path):
    
    drone_positions = {}

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
                    hashed_name = int(hashlib.sha256(vehicle_name.encode()).hexdigest(), 16) % 0xffffff
                    color = (hashed_name & 0xFF, (hashed_name >> 8) & 0xFF, (hashed_name >> 16) & 0xFF)
                    if vehicle_name not in drone_positions:
                        drone_positions[vehicle_name] = {"color": color, "positions": []}
                    drone_positions[vehicle_name]["positions"] = [(x_center + x, y_center + y)]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return drone_positions
            background.fill((255, 255, 255))
            for vehicle_name, data in drone_positions.items():
                positions = data["positions"]
                if len(positions) >= 2:
                    pygame.draw.lines(background, data["color"], False, positions, 2)
                else:
                    print("Not enough points to draw lines.")
            for vehicle_name, data in drone_positions.items():
                current_position = data["positions"][-1]
                pygame.draw.circle(background, data["color"], current_position, 5, 5)
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
