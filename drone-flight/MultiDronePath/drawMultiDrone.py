
import time
import pygame
import hashlib  # 드론 이름을 해시값으로 변환하기 위해 필요한 모듈

#꼬리 없이 경로 그리기(그라데이션 x)

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
                    # 드론의 이름을 추출
                    vehicle_name = line.split(" ")[0]
                    
                    # coordinates_str 변수에 드론의 위치 정보를 포함한 부분을 저장
                    coordinates_str = line.split(":")[1].strip()
                    x_str, y_str = coordinates_str.split(",")
                    x = float(x_str.strip())
                    y = float(y_str.strip())
                    print(f"{vehicle_name} - x_position: {x}, y_position: {y}")

                    # 드론 이름을 해시값으로 변환하여 동적으로 색상 부여 => 드론마다 각기 다른 색상 랜덤부여
                    hashed_name = int(hashlib.sha256(vehicle_name.encode()).hexdigest(), 16) % 0xffffff
                    color = (hashed_name & 0xFF, (hashed_name >> 8) & 0xFF, (hashed_name >> 16) & 0xFF)

                    # drone_positions 딕셔너리에 드론의 이름을 키로 하여 해당 드론의 색상과 위치 정보 저장
                    if vehicle_name not in drone_positions:
                        drone_positions[vehicle_name] = {"color": color, "positions": []}

                    # 현재 위치를 해당 드론의 positions 리스트에 추가
                    drone_positions[vehicle_name]["positions"] = [(x_center + x, y_center + y)]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return drone_positions

            background.fill((255, 255, 255))

            # 각 드론 별로 선 그리기
            for vehicle_name, data in drone_positions.items():
                positions = data["positions"]
                if len(positions) >= 2:
                    pygame.draw.lines(background, data["color"], False, positions, 2)

                else:
                    print("Not enough points to draw lines.")

            # 각 드론 별로 현재 위치에 원 그리기
            for vehicle_name, data in drone_positions.items():
                current_position = data["positions"][-1]   #가장 최근에 저장된 위치값
                pygame.draw.circle(background, data["color"], current_position, 5, 5)

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
