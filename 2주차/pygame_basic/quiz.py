'''
Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동가능
2. 동은 화면 가장 위에서 떨어짐, x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - background.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70 * 70 - enemy.png
'''

import pygame
import random
##############################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

# 화면 크기 설정

screen_width = 480 # 가로크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("ddong pihagi Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
#################################################################################################

# 1. 사용자 게임 초기화 (배경화면 게임 이미지, 좌표, 속도, 폰트 등)

# 배경화면 정의
background = pygame.image.load("C:/Users/pc/나도코딩/2주차/pygame_basic/background.png")

# 캐릭터 정의
character = pygame.image.load("C:/Users/pc/나도코딩/2주차/pygame_basic/character.png")
character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]

# 캐릭터 초기화 위치
character_x_pos = (screen_width - character_width) / 2
character_y_pos = (screen_height - character_height)

# DDong 정의
DDong = pygame.image.load("C:/Users/pc/나도코딩/2주차/pygame_basic/DDong.png")
DDong_size = DDong.get_size()
DDong_width = DDong_size[0]
DDong_height = DDong_size[1]

# DDong 초기화 위치
DDong_x_pos = random.randint(0, screen_width - DDong_width)
DDong_y_pos = 0

# character 이동 좌표 및 속도
to_x = 0
to_y = 0
character_speed = 1

# DDong 좌표 및 이동 속도
DDong_y = 1
DDong_speed = 0.3

# 총 게임 시간
total_time = 10

# timer
start_time = pygame.time.get_ticks()

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 포트 객체 생성 (폰트, 크기)

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 왼쪽으로 이동
                to_x -= character_speed # 
            elif event.key == pygame.K_RIGHT: # 오른쪽으로 이동
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width

    # 4. DDong 움직임
    DDong_y_pos += DDong_speed * dt
    if DDong_y_pos >= screen_height - DDong_height :
        DDong_x_pos = random.randint(0, screen_width - DDong_width)
        DDong_y_pos = 0

    # 5. 충돌 처리
    character_rect = character.get_rect()  # 충돌 처리를 위한 rect 정보 업데이트
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    DDong_rect = DDong.get_rect()
    DDong_rect.left = DDong_x_pos
    DDong_rect.top = DDong_y_pos

    # 충돌 체크
    if character_rect.colliderect(DDong_rect):
        print("충돌했어요")
        running = False

    # timer 그리기
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255, 255, 255))
    if total_time - elapsed_time <= 0:  # 만약 시간이 0 이하이면 게임 종료
        print("타임아웃")
        running = False
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(DDong, (DDong_x_pos, DDong_y_pos))
    screen.blit(timer, (10,10))


    pygame.display.update()

# 2초 대기 후 종료
pygame.time.delay(2000)

pygame.quit()