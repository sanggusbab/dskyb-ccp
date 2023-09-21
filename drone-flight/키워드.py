# def profile(name,age,main_lag):
#     print(name, age, main_lag)

# profile(name="유재석", main_lag="파이썬", age=20)
# profile( main_lag="파이썬", age=25, name="김태호")


# def profile(name, age, lang1, lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20,"파이썬", "자바", "C", "C++", "C#")
# profile("김태호", 25, "kotlin", "swift", "", "", "")

#가변인자
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20,"파이썬", "자바", "C", "C++", "C#", "자바스크립트")
profile("김태호", 25, "kotlin", "swift", "", "", "")