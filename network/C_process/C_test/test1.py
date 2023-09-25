# edge 좌표 정보
edge = [
    {"x": 1, "y": 4, "value": "A"},
    {"x": 5, "y": 5, "value": "B"},
    {"x": 1, "y": 1, "value": "C"},
    {"x": 2, "y": -7, "value": "D"},
    {"x": -6, "y": 3, "value": "E"},
]

position_x = 3
position_y = 3

# task위치 position_x,y가 주어졌을때 edge 탐색할 범위
rect_left = position_x - 2
rect_bottom = position_y - 2
rect_right = position_x + 2
rect_top = position_y + 2

# 원하는 영역의 좌표 (x1, y1)에서 (x2, y2)까지
x1, y1, x2, y2 = rect_left, rect_bottom, rect_right, rect_top

# 영역 안에 있는 edge를 찾는 함수
def find_edge_in_area(edge, x1, y1, x2, y2):
    result = []
    for item in edge:
        x, y = item["x"], item["y"]
        if x1 <= x <= x2 and y1 <= y <= y2:
            result.append(item)
    return result

# 영역 안에 있는 데이터 찾기
result = find_edge_in_area(edge, x1, y1, x2, y2)

# 결과 출력
print("주변에 있는 드론 정보:")
for item in result:
    print(f"x: {item['x']}, y: {item['y']}, value: {item['value']}")