import pygame
from pygame.locals import *
import sys
import gamepage
import map

def main():

    MENU_STATE="title"
    TARGET_FPS = 30
    RED=(255,255,0)
    LEFT=1
    backgroundImages=['./res/background.png','./res/background2.png','./res/background3.png']
    backgroundImage=backgroundImages[0]
    clock = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode((700, 700), DOUBLEBUF)
    pygame.display.set_caption('Hello World!')  # 타이틀바의 텍스트를 설정

    # 2) 화면 해상도를 480*320, 전체 화면 모드, 하드웨어 가속 사용, 더블 버퍼 모드로 초기화하는 경우
    #screen = pygame.display.set_mode((480, 320), FULLSCREEN | HWSURFACE | DOUBLEBUF)

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #if not hasattr(event, 'key'):                    # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
                #continue
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    pass
                elif event.key == K_LEFT:
                    pass
                elif event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass
                elif event.key == K_ESCAPE:
                    pass
            if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                pass
            elif event.type== MOUSEBUTTONUP and event.button==LEFT:
                if MENU_STATE=="title":
                    print("(%d,%d)" %event.pos)
                    if 200<event.pos[0] and event.pos[0]<500 and 300<event.pos[1] and event.pos[1]<400:
                        print("click")
                        gamepage.game(TARGET_FPS,LEFT,backgroundImage)
                    elif 200<event.pos[0] and event.pos[0]<500 and 500<event.pos[1] and event.pos[1]<600:
                        MENU_STATE="background"
                        print("click")

                elif MENU_STATE=="background":
                    print("event background")
                    if 105<event.pos[0] and event.pos[0]<255 and 300<event.pos[1] and event.pos[1]<450:
                        backgroundImage=backgroundImages[0]
                    elif 275<event.pos[0] and event.pos[0]<425 and 300<event.pos[1] and event.pos[1]<450:
                        backgroundImage=backgroundImages[1]
                    elif 445<event.pos[0] and event.pos[0]<595 and 300<event.pos[1] and event.pos[1]<450:
                        backgroundImage=backgroundImages[2]
                    elif 200<event.pos[0] and event.pos[0]<500 and 550<event.pos[1] and event.pos[1]<650:
                        MENU_STATE="title"




        # 게임의 상태를 업데이트하는 부분

        # 게임의 상태를 화면에 그려주는 부분 -> 화면을 지우고, 그리고, 업데이트하는 코드가 들어감
        img = pygame.image.load(backgroundImage)
        screen.blit(img, (0, 0))

        img = pygame.image.load('./res/title.png')
        screen.blit(img, (25, 100))

        if MENU_STATE=="title":

            #img=pygame.draw.rect(screen,RED, (200, 300, 300, 100))
            img = pygame.image.load('./res/start.png')
            screen.blit(img, (200, 300))

            #img=pygame.draw.rect(screen,RED, (200, 500, 300, 100))
            img = pygame.image.load('./res/setbackground.png')
            screen.blit(img, (200, 500))

        elif MENU_STATE=="background":
            img = pygame.image.load('./res/smallbackground.png')
            screen.blit(img, (105, 300))

            fontObj = pygame.font.Font(None,32)                # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
            textSurfaceObj = fontObj.render("background1", True, (255,255,255))   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
            textRectObj = textSurfaceObj.get_rect();                      # 텍스트 객체의 출력 위치를 가져온다
            textRectObj.center = (180, 500)                               # 텍스트 객체의 출력 중심 좌표를 설정한다
            screen.blit(textSurfaceObj, textRectObj)

            #img=pygame.draw.rect(screen,RED, (200, 500, 300, 100))
            img = pygame.image.load('./res/smallbackground2.png')
            screen.blit(img, (275, 300))

            fontObj = pygame.font.Font(None,32)                # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
            textSurfaceObj = fontObj.render("background2", True, (255,255,255))   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
            textRectObj = textSurfaceObj.get_rect();                      # 텍스트 객체의 출력 위치를 가져온다
            textRectObj.center = (350, 500)                               # 텍스트 객체의 출력 중심 좌표를 설정한다
            screen.blit(textSurfaceObj, textRectObj)

            img = pygame.image.load('./res/smallbackground3.png')
            screen.blit(img, (445, 300))

            fontObj = pygame.font.Font(None,32)                # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
            textSurfaceObj = fontObj.render("background3", True, (255,255,255))   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
            textRectObj = textSurfaceObj.get_rect();                      # 텍스트 객체의 출력 위치를 가져온다
            textRectObj.center = (520, 500)                               # 텍스트 객체의 출력 중심 좌표를 설정한다
            screen.blit(textSurfaceObj, textRectObj)

            img = pygame.image.load('./res/ok.png')
            screen.blit(img, (200, 550))



        pygame.display.flip()  # 화면 전체를 업데이트
        clock.tick(TARGET_FPS)  # 프레임 수 맞추기
    pass

if __name__=="__main__":
    main()
