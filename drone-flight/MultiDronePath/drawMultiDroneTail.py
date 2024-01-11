
import time
import pygame
from collections import deque

#경로를 실시간으로 그리기

pygame.init()  

background = pygame.display.set_mode((960, 720))
pygame.display.set_caption('PYGAME_2')

x_center = background.get_size()[0] // 2
y_center = background.get_size()[1] // 2


def extract_coordinates_from_string(file_path):
    
    drone_positions = {}
    max_positions = 20
    count = 0
    color_intensity = 0 
    
    while True:
        try: 
            with open(file_path, 'r') as file:
                for line in file:
                    # 드론의 이름을 추출
                    vehicle_name = line.split(" ")[0]
                    
                    # coordinates_str 변수에 드론의 위치 정보를 포함한 부분을 저장
                    coordinates_str = line.split(":")[1].strip()
                    x_str, y_str = coordinates_str.split(",")
                    x = float(x_str.strip())
                    y = float(y_str.strip())
                    print(f"{vehicle_name} - x_position: {x}, y_position: {y}")

                    #드론별로 색깔을 다르게 하기 위함. 아직까지는 총 7개의 드론까지만 색 할당가능
                    color = [
                        (255,color_intensity, color_intensity),  #빨강
                        (color_intensity, 255, color_intensity),  #초록
                        (color_intensity, color_intensity, 255),  #파랑
                        (255, 255, color_intensity),   #노랑
                        (255, color_intensity, 255),     #핑크
                        (color_intensity, 255, 255),       #민트
                        (color_intensity, color_intensity, color_intensity)  #검정
                    ]

                    # drone_positions 딕셔너리에 드론의 이름을 키로 하여 해당 드론의 색상과 위치 정보 저장(20개 제한 queue)
                    if vehicle_name not in drone_positions:
                        drone_positions[vehicle_name] = {"color": color[count], "positions": deque(maxlen=max_positions)}
                        count= count +1
                        print(drone_positions[vehicle_name]["color"])

                    # 현재 위치를 해당 드론의 positions 리스트에 추가
                    drone_positions[vehicle_name]["positions"].append((x_center + x, y_center + y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return drone_positions

            background.fill((255, 255, 255))

            # 각 드론 별로 현재 위치에 원 그리기
            for vehicle_name, data in drone_positions.items():
                current_position = data["positions"][-1]   #가장 최근에 저장된 위치값
                pygame.draw.circle(background, data["color"], current_position, 5, 5)



            # 각 드론 별로 선 그리기
            for vehicle_name, data in drone_positions.items():
                positions = data["positions"]
        
                
                if len(positions) >= 2:
                    for i in range(len(positions) - 1):
                        color_intensity = 230-i*10     # (230,230,255)연하늘 -> (0,0,255) 쨍한 파란색
                        print(f"color_indensity: {color_intensity}")

                        #color_intensity를 "color" 튜플값에 반영하기 위해 리스트화한 후, color_intensity 반영 후 다시 튜플로 바꿈.
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
            

            pygame.draw.line(background, (0, 0, 0), (x_center, 0), (x_center, y_center * 2))
            pygame.draw.line(background, (0, 0, 0), (0, y_center), (x_center * 2, y_center))
            pygame.display.update()

            time.sleep(1)

        except FileNotFoundError:
            print(f"File not found: {file_path}")
            break

def main():
    output_file_path = "C:/Users/dlwng/Downloads/DronePositions.txt"

    while True:
        extract_coordinates_from_string(output_file_path)


if __name__ == "__main__":
    main()
