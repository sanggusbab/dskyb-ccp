absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent :
        continue #아래 명령을 따르지 않고 for문 다음으로 넘어감
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break #아예 끝내버림
    print("{0}, 책 읽어봐".format(student))