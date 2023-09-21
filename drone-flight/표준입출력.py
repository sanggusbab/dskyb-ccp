print("Python","Java", sep=".")
print("Python","Java", sep=" ")
print("Python","Java", sep=" vs ")
print("Python","Java", sep=", ", end="? ")#end는 줄바꿈 안하고 바로 출력
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

score = {"수학":0, "영어": 50, "코딩":100}
for subject, score in score.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")


#은행 대기순번표
#001, 002. ...
for num in range (1,21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " +answer+"입니다.")