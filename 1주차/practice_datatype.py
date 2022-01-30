'''숫자형'''
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

'''문자형'''
# print('풍선')
# print("나비")
# print("ㅋ"*9)

'''boolean 참/거짓'''
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not (5 > 10))

'''변수- 애완동물을 소개해 주세요'''

# print("우리집 강아지의 이름은 연탄이에여")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일가요? True")

# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = (age >= 3)

# print("우리집" + animal + "의 이름은" + name + "에여")
# print(name + "는" +str(age) +"살이며," + hobby + "을 아주 좋아해요")
# print(name + "는 어른일가요?" + str(is_adult))

'''쉼표도 가능 대신 빈칸이 같이 들어감'''
# animal = "고양이"
# name = "까망이"
# age = 2
# hobby = "놀이"
# is_adult = (age >= 3)

# print("우리집",animal,"의 이름은",name,"에여")
# print(name, "는",str(age) ,"살이며,",hobby, "을 아주 좋아해요")
# print(name, "는 어른일가요?" ,str(is_adult))

'''
Quiz1) 변수를 이용하여 다음 문장을 출력하시오

변수명:
    station
변수값:
    "사당", "신도림", "인천공항" 순서대로 입력
출력 문장:
    XX 행 열차가 들어오고 있습니다.

'''

# station = "사당"
# print(station+"행 열차가 들어오고 있습니다")

# station = "신도림"
# print(station+"행 열차가 들어오고 있습니다")

# station = "인천공항"
# print(station+"행 열차가 들어오고 있습니다")

'''숫자형 deep'''

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3) #2^3=8
# print(5%3) # 나머지 구하기
# print(10%3)
# print(5//3) # 몫 구하기
# print(10//3)

# print(10 > 3)
# print(4 >= 7)
# print(10 <3 )
# print( 5<=5)

# print( 3 == 3)
# print( 4 == 2)

# print(1 != 3)
# print(not(1 != 3))

# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True

# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True

# print(5 > 4 > 3) 
# print(5 > 4 > 7)

'''간단한 수식'''
# print( 2 + 3*4) #14
# print((2+3) * 4) # 20
# number = 2 + 3*4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)

# number %= 5
# print(number)

'''숫자 처리 함수'''
# print(abs(-5)) #절대값 

# print(pow(4,2)) # 4^2 = 16
# print(max(5, 12)) #12
# print(min(5,11)) #5
# print(round(3.14)) #반올림
# print(round(4.99))

# from math import *

# print(floor(4.99)) # 내림
# print(ceil(3.14)) # 올림
# print(sqrt(16)) # 제곱근

'''랜덤함수'''

# from random import *

# print(random()) # 랜덤함수로 0.0~1.0미만의 난수 출력
# print(random()*10)
# print(int(random()*10))
# print(int(random()*10)+1)

# print(int(random() *45)+1)
# print(int(random() *45)+1)
# print(int(random() *45)+1)
# print(int(random() *45)+1)
# print(int(random() *45)+1)
# print(int(random() *45)+1)

# print(randrange(1,46)) #1~46 미만의 임의의 값 생성

# print(randint(1,45)) # 1~45 이하의 임의의 값생성
# print(randint(1,45)) # 1~45 이하의 임의의 값생성
# print(randint(1,45)) # 1~45 이하의 임의의 값생성
# print(randint(1,45)) # 1~45 이하의 임의의 값생성
# print(randint(1,45)) # 1~45 이하의 임의의 값생성
# print(randint(1,45)) # 1~45 이하의 임의의 값생성

'''
Quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞은 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1: 랜덤으로 날짜를 뽑아야함
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.

'''
# from random import *
# study = randint(4,28)
# print("오프라인 스터디 모임 날자는 매월", str(study) +"일로 선정되었습니다.") 

'''문자열'''
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "990120-1234567"

# print("성별 : "+jumin[7])
# print("연 : "+jumin[0:2])
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일 : "+jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 : "+jumin[7:]) #7부터 끝까지

# print("뒤 7자리(뒤에부터) : "+jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

'''문자열 처리 함수'''

# python = "Python is Amazing"
# print(python.lower()) # 전체 소문자
# print(python.upper()) # 전체 대문자
# print(python[0].isupper()) # 0번째 문자가 대문자이니?
# print(len(python)) #python의 문자열 길이
# print(python.replace("Python", "Java")) #문자열 변환

# index = python.index("n")
# print(index) # 문자의 위치 index값 반환 

# index = python.index("n", index + 1) # n중에 다음 번째 n 찾아줌
# print(index) # 문자의 위치 index값 반환 

# print(python.find("Java")) # 원하는 값이 없으면 -1 값 반환 프로그램은 계속 진행
# # print(python.index('java')) # error가 뜨면서 프로그램 종료
# print("hi")

# print(python.count("n")) #n이라는 문자가 몇번나왔는지 확인

"""문자열 포맷"""

# #방법1 :  %를 활용
# print("나는 %d살입니다."%20) #d는 정수
# print("나는 %s을 좋아합니다. "%"파이싼") #s는 문자열
# print("Apple은 %c로 시작해요."%"A") #c는 문자 하나

# print("나는 %s색과 %s색을 좋아해여" %("파란", "빨간"))

# #방법2 : format함수
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해.".format("파란", '빨간'))

# print("나는 {0}색과 {1}색을 좋아해.".format("파란", '빨간')) #index로 순서를 바꿀 수도 있음
# print("나는 {1}색과 {0}색을 좋아해.".format("파란", '빨간'))

# print("나는 {age}살이며 {color}색을 좋아해.".format(age =20, color = '빨간')) # 변수로 지정해줄 수 있음

# 방법3 (v3.6 이상~)

# age =20
# color ="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")#변수를 그대로 들고 올 수 있음

'''탈출 문자'''
# print("백문이 불여일견 \n 백견이 불여일타")

# # 저는 "나도코딩"입니다.
# # print("저는 "나도코딩"입니다")
# print('저는 "나도코딩"입니다')
# print("저는 \"나도코딩\"입니다")

# # \\: 문장 내에서 \
# print("C:\\Users\\pc\\나도코딩")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

'''
Quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

예) 생성된 비밀번호 :nav51!
'''
# 내 방법
# string = "http://naver.com"
# n_index = string.index("n")
# dot_index = string.find(".")

# sorting_string = string[n_index:dot_index]
# password = sorting_string[:3] + str(len(sorting_string)) + str(sorting_string.count("e")) +"!"  
# print(password)

# 나도코딩 방법
# url = "http://naver.com"
# my_str = url.replace("http://","") # 규칙1
# print(my_str)
# my_str = my_str[:my_str.index(".")] #규칙2
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))

'''리스트'''
# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

# subway1 =10
# subway2 =20
# subway3 =30

# subway = [10,20,30]
# print(subway)

# name = ["유재석", "조세호", "박명수"]

# #조세호씨가 몇번째 칸에 타고 있는가?

# print(name.index("조세호"))

# name.append("하하")
# print(name)

# name.insert(1,"정형돈")
# print(name)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

# print(name.pop())
# print(name)

# print(name.pop())
# print(name)

# print(name.pop())
# print(name)

# print(name.pop())
# print(name)

#같은 이름의 사람이 몇 명 있는지 확인
# name.append("유재석")
# print(name)

# print(name.count("유재석"))

# 정렬도 가능 

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# num_list = [5,2,4,3,1]

# mix_list = ["유재석", 20, True]
# print(mix_list)

# num_list.extend(mix_list)
# print(num_list)

'''사전형 자료형'''

# cabinet = {3: "유재석", 100 : "김태호"}
# print(cabinet)
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))

# # print(cabinet[5]) # 오류나고 프로그램 종료
# # print("hi")

# print(cabinet.get(5)) # None값 반환하고 프로그램 진행
# print("hi")


# print(cabinet.get(5,"사용가능")) # 뒤에 문자열값(사용가능) 반환하고 프로그램 진행
# print("hi")

# print(3 in cabinet) # key값에 3이 있니
# print(5 in cabinet)

# cabinet = {"A-3": "유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새손님
# print(cabinet)

# cabinet["A-30"] = "김종국"
# cabinet["C-20"] = "조세호"

# print(cabinet)

# cabinet["A-3"] = "김종국"
# print(cabinet)

# # 간 손님

# del cabinet['A-3']
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet.values())

# # key, value 둘다 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# '''튜플'''

# # 변경하지 않는 자료형

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# #menu.add("생선까스") # add를 지원하지 않음

# name, age, hobby = "김종국", 20, "코딩"
# print(name,age, hobby)

# '''세트 - 집합'''

# #중복이 안되고, 순서가 없음

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", '박명수'])

# #교집합 
# print(java & python)
# print(java.intersection(python))

# #합집합

# print(java | python)
# print(java.union(python))

# #차집합 (java 가능 python 불가능 개발자)
# print(java - python)
# print(java.difference(python))

# #python 할줄 아는 사람 늘어나

# python.add("김태호")
# print(python)

# #java를 잊엇어요
# python.remove("김태호")
# print(python)

'''자료 구조의 변경'''

# menu = {"커피", "우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

'''
Quiz4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

조건1: 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
조건3: random 모듈의 shuffle 과 sample을 활용

(출력예제)
--당첨자 발표--
치킨 당첨자 : 1
커피 당첨자:[2,3,4]
--축하합니다--
'''

#(활용예제)

# from random import *

# lst = [ 1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

# 내방법
# from random import *

# list = list(range(1,21))
# shuffle(list)
# chi = list.pop()
# shuffle(list)
# coffee = sample(list,3)
# # print(chi, coffee)

# print("-- 당첨자 발표 --\n치킨 당첨자 : {}\n커피 당첨자 : {}\n--축하합니다--".format(chi, coffee))

# 나도코딩 방법

from random import *

users =range(1,21)
# print(type(users))
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)

winners =sample(users,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. --")