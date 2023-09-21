#출석번호가 1 2 3 4, 앞에 10붙이기로 함

students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students =[len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students =[i.upper() for i in students]
print(students)

#quiz
from random import*

customer = 0
count=0

while customer <=50 :
    time = randint (5,51)
    if 5<= time <=15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
        count +=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
    customer+=1

    # print (customer)
    # print (time)

print(count)



