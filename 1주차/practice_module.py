'''모듈'''
# 모듈은 사용하려는 파일의 같은 디렉토리안에 있어야 함, py파일 자체
# import theater_module

# theater_module.price(3) # 3명이서 영화보러 갔을 대 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화보러 갔을 떄 
# theater_module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때 

# import theater_module as mv

# mv.price(3)
# mv.price_soldier(5)
# mv.price_morning(4)

# from theater_module import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning

# price(3)
# price_morning(4)

# from theater_module import price_soldier as price

# price(10)

'''패키지'''

# travel 패키지를 만들어보자, travel 폴더에 thailand, vietnam, __init__ 모듈

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # class를 import 가능

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

'''__all__'''

# from travel import * # 모듈 

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_to1 = thailand.ThailandPackage()
# trip_to1.detail()

'''모듈 직접 실행''' # if __name__ = "__main__"으로 모듈 내부에서 직접 실행가능
# from travel import * # 모듈 

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_to1 = thailand.ThailandPackage()
# trip_to1.detail()

'''패키지, 모듈 위치'''
# from travel import * # 모듈 

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

'''pip install'''
# www.pypi.org

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


'''내장 함수'''

# input : 사용자 입력을 받는 함수

# language = input("무슨 언어를 좋아하세요?")
# print("{}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 대 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# # print(dir())
# # import pickle
# # print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst)), 'list of python builtins' google에서 검색

# name = "jim"
# print(dir(name))


'''외장함수 list of python modules 검색'''

# glob : 경로 내의 폴더 . 파일 목록 조회 (윈도우 dir과 유사)

# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본기능

import os
# print(os.getcwd())
# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())


# time : 시간 관련 함수

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# # print("오늘 날자는 ", datetime.date.today())

# #timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날자 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td)


'''
Quiz10) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졋습니다.
유튜브 : ~~
이메일 : ~~
'''

import byme

byme.sign()