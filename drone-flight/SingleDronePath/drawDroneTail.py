import time
import pygame
from collections import deque

#점 찍기+ 경로 표시
#background 확대 

pygame.init()  

#background 확대하려면 set_mode(( , ))의 값만 바꿔주면 됨.
background = pygame.display.set_mode((960, 720))   
pygame.display.set_caption('PYGAME_2')

# 중심 좌표
x_center = background.get_size()[0]//2 # 480
y_center = background.get_size()[1]//2 # 360

#드론 위치를 저장할 큐 초기화
drone_positions = deque(maxlen=20)

def extract_coordinates_from_string(file_path):

 while True:
    try: 
      with open(file_path, 'r') as file:
        line = file.readline()
        # "Drone Position: x, y, z" 형식의 문자열에서 "x, y" 부분 추출
        coordinates_str = line.split(":")[1].strip()

        # 추출된 문자열을 쉼표로 분리하여 각각의 값을 얻음
        x_str, y_str= coordinates_str.split(",")

        # 문자열을 부동 소수점 수로 변환
        x = float(x_str.strip())
        y = float(y_str.strip())

        print("x_position: ", x)
        print("y_position: ", y)

        #현재 위치를 드론 위치 리스트에 추가
        drone_positions.append((x_center+x,y_center+y))

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            play = False

        background.fill((255,255,255))

        # 원으로 드론 현재 위치 표시
        # pygame.draw.circle(화면, 색, 중심 좌표(평면에서의 origin은 (x_center, y_center)이므로 각각에 x,y더해줌), 반지름, 선 굵기) 
        pygame.draw.circle(background, (255,0,0), (x_center+x,y_center+y), 5, 5)
        

        # 드론 경로 그리기(위치 정보가 2개 이상 모여야 경로 그리기 가능)
        # pygame.draw.line(화면, 색, 시작 위치, 끝 위치, 선 굵기) 
        if len(drone_positions) >= 2:
          
              for i in range(len(drone_positions) - 1):
                color_intensity = 230-i*10     # (230,230,255)연하늘 -> (0,0,255) 쨍한 파란색
                color = (color_intensity, color_intensity, 255)
                pygame.draw.line(background, color, drone_positions[i], drone_positions[i+1], 7)

        else:
          print("Not enough points to draw lines.")

        # 중심점 기준으로 선 그려주기
        pygame.draw.line(background, (0,0,0), (x_center,0), (x_center,y_center*2))
        pygame.draw.line(background, (0,0,0), (0,y_center), (x_center*2,y_center))
        pygame.display.update()

        time.sleep(1)  #time.sleep(0.5)로 하면 좀 더 자연스러운 꼬리가 됨.

    except FileNotFoundError:
      print(f"File not found: {file_path}")
      break
    

output_file_path = "C:/Users/dlwng/Downloads/DronePosition.txt"

extract_coordinates_from_string(output_file_path)

pygame.quit()

