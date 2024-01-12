
import time
import pygame
import sys
from collections import deque

#경로를 실시간으로 그리기 + 꼬리 그리기 + 드론이미지

pygame.init()  

#background 확대하려면 set_mode(( , ))의 값만 바꿔주면 됨.
background = pygame.display.set_mode((960, 720))
pygame.display.set_caption('PYGAME_2')

# 중심 좌표
x_center = background.get_size()[0] // 2
y_center = background.get_size()[1] // 2


# 이미지 로드
image_path = "drone.png"  # 사용하려는 이미지 파일의 경로
original_image = pygame.image.load(image_path)
image_rect = original_image.get_rect()

# 이미지 크기 조절
new_width, new_height = 40, 40  # 원하는 크기로 조절
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

            #각 드론별로 이미지를 현재 위치에 그림
            #현재위치 - new_height/2 를 각각 해주어야 꼬리가 드론 중앙에 생김.아니면 꼬리가 드론의 꼭짓점에 생기게 됨.
            #경로 line을 먼저 그리고 드론을 그려줘야 드론과 경로가 겹쳐보이지 않음.

            for vehicle_name, data in drone_positions.items():
                current_position = data["positions"][-1]   #가장 최근에 저장된 위치값
                background.blit(resized_image, current_position)
            

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
