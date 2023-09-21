gun=10

def checkpoint(soldiers): #경계근무
    global gun #전역공간에 있는 gu 사용
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #바뀐 gun 값을 외부로 던짐

print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 :{0}".format(gun))

#quiz
def std_weight(height, gender):
    if gender == 0: #여자
        print("키 {0}cm 여자의 표준 체중은 {1}입니다.".format(height, height*height*0.01*21//1*0.01))
        return height*height*21
    elif gender == 1: #남자
        print("키 {0}cm 남자의 표준 체중은 {1}입니다.".format(height, height*height*0.01*22//1*0.01))
    
std_weight(height=175,gender = 1)
std_weight(height=165,gender = 0)
std_weight(height=177,gender = 1)