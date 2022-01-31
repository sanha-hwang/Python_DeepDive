# 마린 : 공격유닛, 군인, 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {}, 공격력 {}\n".format(hp, damage))

# 탱크 : 공격 유닛 , 탱크, 포를 쏠 수 있는 데, 일반모드 /시즈모드

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(\
#         name, location, damage))
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name # 멤버변수들
#         self.hp = hp
#         self.damage = damage
#         print("{}유닛이 생성되었습니다.".format(self.name))
#         print("체력 {}, 공격력 {}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 레이스 : 공중 유닛 ,비행기, 클로킹(상대방에게 보이지 않음)

# wraith1 = Unit(" 빼앗은 레이스", 80,5)
# print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)

# wraith2  = Unit("레이스", 80,5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.clocking))

# '''매소드'''

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name # 멤버변수들
#         self.hp = hp
        
# # 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name =name
#         self.hp = hp
#         self.damage=damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입엇습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되엇습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염 방사기

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정

# firebat1.damaged(25)

# firebat1.damaged(25)

'''상속'''

# 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name # 멤버변수들
#         self.hp = hp
        
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage=damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입엇습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되엇습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정

# firebat1.damaged(25)

# firebat1.damaged(25)


'''다중 상속'''

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name # 멤버변수들
#         self.hp = hp
        
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage=damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입엇습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되엇습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃/ 탱크 등을 수송, 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
    


# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

'''연산자 오버라이딩'''

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name # 멤버변수들
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))
        
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage=damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입엇습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되엇습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃/ 탱크 등을 수송, 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp,0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecrusier.move("9시")

'''pass'''
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name # 멤버변수들
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))
        
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage=damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입엇습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되엇습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃/ 탱크 등을 수송, 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp,0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 지나가기

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supplt_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

'''super'''
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name # 멤버변수들
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))
        
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage=damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입엇습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되엇습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃/ 탱크 등을 수송, 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp,0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp,0)
#         super().__init__(name, hp,0) # self없이 상속받기 but  다중상속일 때 문제가 생김
#         self.location = location
# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supplt_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         # super().__init__()  # 맨 처음의 상속 받는 class의 init 불러옴
#         Unit.__init(self)
#         Flyable.__init__(self)

'''
Quiz9) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

'''

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, \
            self.price, self.completion_year))
        
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2010년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {}대의 매물이 있습니다.".format(len(houses)))
for h in houses:
    h.show_detail()