# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# '''전달값과 반환값'''
# def deposit(balance, money): #  입금
#     print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance + money))
    
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {}원입니다.".format(balance))
#         return balance
    
# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100
#     return commission, balance-money-commission

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)
# # balance = withdraw(balance, 2000)
# # balance - withdraw(balance, 200)

# commission, balance = withdraw_night(balance, 500)
# print("수수료 {}원이며, 잔액은 {}원입니다.".format(commission, balance))







'''기본값'''
# def profile(name, age, main_lang):
#     print("이름: {}\t 나이 : {}\t 주 사용 언어: {}" \
#         .format(name,age,main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang='파이썬'):
#     print("이름: {}\t 나이 : {}\t 주 사용 언어: {}" \
#         .format(name,age,main_lang))

# profile("유재석")
# profile("김태호", main_lang='자바')

'''키워드값'''


# def profile(name, age, main_lang):
#     print("이름: {}\t 나이 : {}\t 주 사용 언어: {}" \
#         .format(name,age,main_lang))

# profile(name = "유재석", main_lang="파이썬", age =20)
# profile("김태호", age =25,  main_lang='자바')

'''가변인자'''

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "python", 'java', "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "swift","","","")


# def profile(name, age, *language):
#     print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end =" ")
#     print()

# profile("유재석", 20, "python", 'java', "C", "C++", "C#", "JS")
# profile("김태호", 25, "Kotlin", "swift")

# '''지역변수와 전역변수'''

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun  사용
#     gun = gun - soldiers #  지역변수 gun이 할당되지 않았음
#     print("[함수내] 남은 총: {}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수내] 남은 총 : {}".format(gun))
#     return gun


# print("전체 총 : {}".format(gun))

# gun = checkpoint_ret(gun, 2) # 2명이 경계 근무 나감
# print("남은 총 : {}".format(gun))



'''
Quiz6) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 다른 공식)
남자: 키(m) x 키(m) x 22
여자: 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명: std_weight
        * 전달값: 키(height), 성별(gender)

조건2 : 표준 체중은 소수점 둘재자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg입니다.
'''

# 내방법
# def std_weight(height, gender):
#     if gender == "남자":
#         recom_weight = (height/100)**2 * 22
#     elif gender == "여자":
#         recom_weight = (height/100)**2 * 21
    
#     return round(recom_weight,2)

# height = int(input("키(cm)를 입력하시오"))
# gender = input("성별을 입력하시오")
# print("키 {} {}의 표준 체중은 {}kg입니다.".format(height, gender, std_weight(height, gender)))

# 나도코딩 방법

# def std_weight(height, gender): #키는 m 단위(실수), 성별 "남자"/"여자"
#     if gender ==  "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100 , gender), 2)
# print("키 {}cm {}의 표준 체중은 {}kg입니다.".format(height, gender, weight))

