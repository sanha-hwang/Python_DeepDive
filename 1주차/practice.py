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

python = "Python is Amazing"
print(python.lower()) # 전체 소문자
print(python.upper()) # 전체 대문자
print(python[0].isupper()) # 0번째 문자가 대문자이니?
print(len(python)) #python의 문자열 길이
print(python.replace("Python", "Java")) #문자열 변환

index = python.index("n")
print(index) # 문자의 위치 index값 반환 

index = python.index("n", index + 1) # n중에 다음 번째 n 찾아줌
print(index) # 문자의 위치 index값 반환 

print(python.find("Java")) # 원하는 값이 없으면 -1 값 반환 프로그램은 계속 진행
# print(python.index('java')) # error가 뜨면서 프로그램 종료
print("hi")

print(python.count("n")) #n이라는 문자가 몇번나왔는지 확인

"""문자열 포맷"""