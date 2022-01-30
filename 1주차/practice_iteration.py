'''for문'''

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호: {0}".format(waiting_no))

# for waiting_no in range(5): # 0~4
#     print("대기번호: {0}".format(waiting_no))

    
# for waiting_no in range(1,6): # 0~4
#     print("대기번호: {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

'''while'''

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1

#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# 무한루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 번째".format(customer, index))
#     index += 1

# customer = "토르"
# person = 'Unknown'

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어덯게 되세요?")


'''continue and break'''

# absent = [2, 5] # 결석
# no_book = [7]

# for student in range(1,11):
#     if student in absent: # 다음 반복문으로 진행
#         continue
#     elif student in no_book: # 반복문 종료
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

'''한줄 for문'''
#
# student = [1,2,3,4,5]
# print(student)
# students = [i + 100 for i in student]
# print(students)

# students = ["Iron man", 'Thor', "I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", 'Thor', "I am groot"]

# students = [i.upper() for i in students]
# print(students)

'''
Quiz5) ekdtlsdms cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 대, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번재 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번재 손님 (소요시간: 16분)

총 탑승 승객 : 2분
'''

# 내 방법
# from random import *

# number = 50 
# count = 0
# for i in range(number):
#     time = randint(5,50)
#     if 5 <= time <= 15:
#         flag = "O"
#         count += 1
#     else:
#         flag =" "
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(flag,i+1,time))
# print("총 탐승 승객 : {}분".format(count))

# 나도코딩 방법

# from random import *
# cnt = 0 # 총 탑승 승객 수

# for i in range(1,51): # 1~50  승객
#     time = randrange(5,51)
#     if 5 <= time <= 15: # 5분~15분 이내의 손님, 탑승 승객 수 증가 처리
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
# print("총 탑승 승객 : {}".format(cnt))