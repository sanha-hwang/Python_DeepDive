import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정

screen_width = 480 # 가로크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/pc/나도코딩/2주차/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False
    #  screen.fill((0,0,255)) # 색깔을 채워넣을 수는 있음
    screen.blit(background, (0,0)) # 배경그리기 튜플은 시작 좌표

    pygame.display.update() # 게임 화면을 다시 그리기(매 프레임 당 계속 그려줘야함)

# pygame 종료
pygame.quit()