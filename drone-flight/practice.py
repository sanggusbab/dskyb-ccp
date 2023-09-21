print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print('풍선')
print("나비")
print("ㅋ"*9)

#분리형 : 참/거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not (5<10))


#애완동물을 소개해주세요~
name = "먼지"
animal = "강아지"
age = 1
hobby = "산책"
is_adult = age >=1

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
#print(name + "는 " +str(age)+ "살이고 " +hobby+ "을 아주 좋아해요")
print(name, "는 " ,age, "살이고 " ,hobby, "을 아주 좋아해요") 
#콤마 사용 가능-->콤마면 str안써도 됨, 대신 띄어쓰기 됨
print(name+ "는 어른일까요? " +str(is_adult))


#quiz

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

print(2**3) #2^3=8
print(5%3) #나머지
print(5//2) #몫

print(1 != 3) #not
print(not(1 != 3))

print ((3>0) & (5>3)) #and
print((3<0) | (5<0)) #or

number=14
print(number)
number= number+2
print(number)
number += 2 #위랑 같은 뜻 *=, /+, -= 다 가능
print(number)

print(abs(-5))
print(pow(4,2)) #4^2=16
print(max(5, 12))
print(min(5,12))
print(round(3.14)) #반올림

from math import* #math 라이브러리 사용하겠다.
print(floor(4.99)) #내림.4
print(ceil(3.14)) #올림.4
print(sqrt(16)) #제곱근.4

from random import*
print(random()) #0.0이상 1.0 미만의 임의의 값 생성
print(random()*10) #0.0 이상 10.0 미만의 임의의 값 생성
print(int(random()*10)) #소숫점 없애줌 0~10
print(int(random()*10)+1) #1~10이하


#로또 추첨
print(randrange(1,46)) #1~45까지 숫자 생성
print(randint(1,45)) #1~45


#quiz
from random import*
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" +str(day)+"일로 선정되었습니다.")


sentence ='나는 소년입니다.'
print(sentence)
sentence2= "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)
#"""는 줄바꿈

jumin="010915-4211111"
print("성별 : " +jumin[7])
print("연도 : " + jumin[0:2]) #0~2 직전까지, 즉 0~1
print("월 : "+jumin[2:4])
print("일 : " +jumin[4:6])

print("생년월일 : " +jumin[:6]) #처음부터 6 직전까지
print("뒷자리 : "+jumin[7:]) #7번째부터 끝까지
print("뒷자리 : "+jumin[-7:]) #맨 끝이 -1임, 맨 뒤에서부터 7까지 부터 끝까지
      

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n") #n이 몇번째 위치인가
print(index)
index = python.index("n", index +1) #index=5에서부터 두번째 n 찾는다
print(index)
print(python.find("n"))
print(python.find("Java")) #포함되어 있지 않은 경우에는 -1이 나옴
#print(python.index("Java"))
print("Hi") #뒤에 출력이 안됨
print(python.count("n"))


#문자열 프린트 방법
#방법1
print("나는 %d살입니다." %20) #d는 정수
print("나는 %s를 좋아합니다." %"python") #s는 문자열
print("Apple은 %c로 시작해요" %"A") #c는 캐릭터라서 한 글자

print("나는 %s살입니다." %20) #s는 다 됨
print ("나는 %s색과 %s색을 좋아합니다." %("파랑","보라"))

#방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다." .format("파랑", "보라"))
print("나는 {0}색과 {2}색을 좋아합니다." .format("파랑", "보라","빨강"))

#방법3
print("나는 {age}살이고 {color}색을 좋아합니다." .format(age=20, color="보라"))

#방법4
age=21
color= "노랑"
print(f"나는 {age}살이고 {color}색을 좋아합니다.")


#탈출문자
print("백문이 불여일견 \n백견이 불여일타") #\n이 줄바꿈
#저는 "이예원"입니다.
print("저는 '이예원'입니다.")
print('저는 "이예원"입니다.')
print("저는 \"이예원\"입니다.") #\"는 문장에서 따옴표로 사용

#\\ 문장 내에서 \
print("c\\Users\\yewon")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\r pine")

#\b : 백스페이스 (한 글자 삭제)
print("Pinee\b Apple")

#\t : 탭
print("Pine\tApple")

#quiz

url = "http://naver.com"
my_str = url.replace("http://","")
print(my_str)

my_str =my_str[:my_str.index(".")]
print(my_str)

password = my_str[:3] + str(len(my_str)) +str(my_str.count("e")) +"!"
print("{0}의 비밀번호는 {1}입니다." .format ("네이버", password))


#리스트
subway =[10, 20, 30]
print(subway)

subway=["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))

#하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

#정형돈을 유재석과 조세호 사이에 넣기
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
max_list = ["조세호", 20, True]
print(max_list)

#리스트 확장
num_list.extend(max_list)
print(num_list)


#사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])
#강제종료
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("Hi")

print(3 in cabinet)
print(5 in cabinet)

cabinet ={ "A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])

#새손님
print(cabinet)
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)


#튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")
#추가 불가

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#세트, 집합
#중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합(자바와 파이썬을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

#합집합(자바를 할 수 있거나 파이썬을 할 수 있는 사람)
print ( java | python)
print(java.union(python))

#차집합 (자바는 할 수 있는데 파이썬은 할 수 없는 사람)
print(java -python)
print (java. difference(python))

#파이썬을 할 수 있는 사람이 늘어남
python.add("김태호")
print(python)

#자바를 까먹었다
java.remove("김태호")
print(java)


#자료구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu =list(menu)
print(menu, type(menu))

menu= tuple(menu)
print(menu, type(menu))

menu= set(menu)
print(menu, type(menu))


#quiz

from random import*
users =range(1,21) #1부터 20까지 숫자를 생성
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 중에서 한명은 치킨 세 명은 커피

print ("--당첨자발표--")
print("치킨 당첨자 :{}".format(winners[0]))
print("커피 당첨자 :{},{}".format(winners[1],winners[2]))
