# def profile(name,age, main_lag):
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어: {2}"\
#           .format(name,age,main_lag))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업
def profile(name,age=17, main_lag="파이썬"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어: {2}"\
          .format(name,age,main_lag))
    
profile("유재석")
profile("김태호")