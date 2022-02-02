'''예외처리'''
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []

#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{} / {} = {}".format(nums[0], nums[1], nums[2]))

# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

'''에러 발생시키기'''

# try:
#     print("한 자리 숫자 나누기 전용 게산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise ValueError
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세여")

'''사용자 정의 예외처리'''

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 게산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2))
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세여")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)

'''finally'''
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 게산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2))
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세여")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:  ## 무조건 실행 
#     print("계산기를 이용해 주셔서 감사합니다.")


'''
Quiz9) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리

출력 메시지 : "잘못된 값을 입력하였습니다."

조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10자리로 한정, 치킨 소진시 사용자 정의[SoldoutError]를
발생시키고 프로그램 종료 
출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다.

[활용 코드]
chicken = 10
waiting = 1  # 홀 안에는현재 만석 대기번호 1부터 시작
while(True):
    print("[남은 치킨 : {}]".format(chicken))
    order = int(input("치킨 몇마리 주문하시겠습니까?"))
    if order > chicken: # 남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")
    else:
        print("[대기 번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
        waiting += 1
        chicken -= order

'''

## 내 방법

# class SoldoutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# chicken = 10
# waiting = 1  # 홀 안에는현재 만석 대기번호 1부터 시작
  
# while(True):
#     print("[남은 치킨 : {}]".format(chicken))
#     try:
#         if chicken <= 0:
#             raise SoldoutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
            
#         order = int(input("치킨 몇마리 주문하시겠습니까?"))
#         if order < 1 or type(order) != int:
#             raise ValueError 
       
#         elif order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#             print("현재 {}마리 치킨 주문가능합니다.".format(chicken))

#         else:
#             print("[대기 번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
                
#     except ValueError:
#         print("잘못된 값을 입력하셨습니다.")
#     except SoldoutError as err:
#         print(err)
#         break
#     finally:
#         print("가게를 찾아주셔서 감사합니다.")


## 나도코딩 방법
class SoldOutError(Exception):
    pass
      

chicken = 10
waiting = 1  # 홀 안에는현재 만석 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
            
        elif order <= 0:
            raise ValueError

        else:
            print("[대기 번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않았습니다.")
        break