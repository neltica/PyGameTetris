import pygame
from pygame.locals import *
import sys
import map
import block
import time

import random

class game:

    clock = pygame.time.Clock()
    TARGET_FPS=''
    LEFT=''
    DOWN_START_TIME=0
    nowBlock=''

    gameScore=0
    ONE_LINE_SCORE=300

    NEXT_ITEM_SHOW_FLAG=False
    itemQueue=[1,1,2,2,3,3]

    MAX_DOWN_CYCLE_TIME=1.0
    DOWN_CYCLE_TIME=1.0
    MIN_DOWN_CYCLE_TIME=0.0
    DOWN_CYCLE_TIME_COUNT=0

    backgroundImage="./res/background.png"
    background = pygame.image.load(backgroundImage)
    itemqueueBackground=pygame.image.load('./res/itemqueue.png')
    itemBackground=pygame.image.load('./res/itembackground.png')
    itemIcon1=pygame.image.load('./res/item1icon.png')
    itemIcon2=pygame.image.load('./res/item2icon.png')
    itemIcon3=pygame.image.load('./res/item3icon.png')
    nextblockbackground=pygame.image.load('./res/nextblock.png')

    def __init__(self,TARGET_FPS,LEFT,backgroundImage):
        print("game __init__")
        self.TARGET_FPS = TARGET_FPS
        self.LEFT=LEFT
        self.itemQueue=[1,1,2,2,3,3]
        self.backgroundImage=backgroundImage
        self.background = pygame.image.load(backgroundImage)
        self.DOWN_CYCLE_TIME=1.0
        self.DOWN_CYCLE_TIME_COUNT=0
        self.gamePlay()
        pass

    def calculateGameScore(self):
        deleteLine=self.mInstance.scoreCheck()
        self.gameScore+=deleteLine*self.ONE_LINE_SCORE

    def downGameSpeed(self):
        self.DOWN_CYCLE_TIME=self.MAX_DOWN_CYCLE_TIME-((self.gameScore/self.ONE_LINE_SCORE)/200)
        print ("gameScore:%f one_line_socre*20:%f total:%f"%(self.gameScore,self.ONE_LINE_SCORE*20,self.gameScore/(self.ONE_LINE_SCORE*20)))
        if self.DOWN_CYCLE_TIME<self.MIN_DOWN_CYCLE_TIME:
            self.DOWN_CYCLE_TIME=self.MIN_DOWN_CYCLE_TIME
        pass

    def isEndGame(self):
        for i in range(0,self.mInstance.mapIndexSize[1],1):
            if self.mInstance.mapData[1][i+2]!=0:
                print("game end")
                return True
        return False

        pass
    def isCrash(self,direction):

        if direction=="left":
            for i in range(0,len(self.nowBlock[0]),1):
                for j in range(0,len(self.nowBlock[0]),1):
                    if self.nowBlock[self.bInstance.blockRotate][i][j]==1:
                        if self.mInstance.mapData[i+self.bInstance.nowPos[0]][j+self.bInstance.nowPos[1]-1]!=0:
                            return True
                        pass
            pass
        elif direction=="right":
            for i in range(0,len(self.nowBlock[0]),1):
                for j in range(0,len(self.nowBlock[0]),1):
                    if self.nowBlock[self.bInstance.blockRotate][i][j]==1:
                        if self.mInstance.mapData[i+self.bInstance.nowPos[0]][j+self.bInstance.nowPos[1]+1]!=0:
                            return True
            pass
        elif direction=="down":
            for i in range(0,len(self.nowBlock[0]),1):
                for j in range(0,len(self.nowBlock[0]),1):
                    if self.nowBlock[self.bInstance.blockRotate][i][j]==1:
                        if self.mInstance.mapData[i+self.bInstance.nowPos[0]+1][j+self.bInstance.nowPos[1]]!=0:
                            #print("(%d,%d)" %(i+self.bInstance.nowPos[0]+1,j+self.bInstance.nowPos[1]),)
                            return True
            pass
        elif direction=="rotate":
            for i in range(0,len(self.nowBlock[0]),1):
                for j in range(0,len(self.nowBlock[0]),1):
                    if self.nowBlock[self.bInstance.blockRotate][i][j]==1:
                        if self.mInstance.mapData[i+self.bInstance.nowPos[0]][j+self.bInstance.nowPos[1]]!=0 or (i+self.bInstance.nowPos[0])<0 or self.mInstance.mapIndexSize[0]+1<(i+self.bInstance.nowPos[0]) or (j+self.bInstance.nowPos[1])<2 or self.mInstance.mapIndexSize[1]+1<(j+self.bInstance.nowPos[1]):
                            return True

        return False

    def eraseBlock(self):
        for i in range(0,len(self.nowBlock[0]),1):
            for j in range(0,len(self.nowBlock[0]),1):
                if self.nowBlock[self.bInstance.blockRotate][i][j]==1:
                    self.mInstance.mapData[i+self.bInstance.nowPos[0]][j+self.bInstance.nowPos[1]]=0


    def insertBlock2Map(self):
        #print("insertBlock2Map",self.nowBlock)
        for i in range(0,len(self.nowBlock[0]),1):   # block drop to map
            for j in range(0,len(self.nowBlock[0]),1):
                if self.mInstance.mapData[i+self.bInstance.nowPos[0]][j+self.bInstance.nowPos[1]]==0 and self.nowBlock[self.bInstance.blockRotate][i][j]==1:
                    self.mInstance.mapData[i+self.bInstance.nowPos[0]][j+self.bInstance.nowPos[1]]=self.bInstance.blockColor+1

        #self.mInstance.printMap()


    def resetBlock(self):
        #print("reset")
        self.NEXT_ITEM_SHOW_FLAG=False
        self.insertBlock2Map()
        self.calculateGameScore()
        self.downGameSpeed()
        self.nowBlock=self.bInstance.reset()
        if self.isCrash("rotate"):
            self.bInstance.nowPos[0]-=1
            if self.isCrash("rotate"):
                print("end Game")
                return True
            else:
                return False
        else:
            return False

        #self.mInstance.printMap()
        print("game score:%d" %self.gameScore)
        print("down_cycle_time_count: %d" %self.DOWN_CYCLE_TIME_COUNT)
        print("game speed:%f"%self.DOWN_CYCLE_TIME)

    def blockRotateUpdate(self):
        self.eraseBlock()
        if self.bInstance.blockIndex!=2:
            self.bInstance.blockRotate+=1
            self.bInstance.blockRotate%=4
            if self.isCrash("rotate"):
                self.bInstance.nowPos[0]-=1
                if self.isCrash("rotate"):
                    self.bInstance.nowPos[0]+=1
                    self.bInstance.blockRotate-=1
                    if self.bInstance.blockRotate<0:
                        self.bInstance.blockRotate=3
                else:
                    self.DOWN_START_TIME=time.time()
            else:
                self.DOWN_START_TIME=time.time()
        else:
            self.DOWN_START_TIME=time.time()

    def blockDownUpdate(self):
        self.eraseBlock()
        if not self.isCrash("down"):
            self.bInstance.nowPos[0]+=1
            self.DOWN_START_TIME=time.time()
            return True
        else:
            print("down crash")
            return False



    def blockLeftUpdate(self):
        self.eraseBlock()
        if not self.isCrash("left"):
            self.bInstance.nowPos[1]-=1
        else:
            print("left crash")


    def blockRightUpdate(self):
        self.eraseBlock()
        if not self.isCrash("right"):
            self.bInstance.nowPos[1]+=1
        else:
            print("right crash")

    def blockSpaceBarUpdate(self,screen,img):
        while True:
            if self.blockDownUpdate():
                self.insertBlock2Map()
                screen.blit(img, (0, 0))

                screen.blit(self.itemqueueBackground,(20,590)) #itemqueuebackground
                screen.blit(self.itemqueueBackground,(20,50)) # score

                fontObj = pygame.font.Font(None,32)                # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
                textSurfaceObj = fontObj.render(str(self.gameScore), True, (255,255,255))   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
                textRectObj = textSurfaceObj.get_rect();                      # 텍스트 객체의 출력 위치를 가져온다
                textRectObj.center = (175, 80)                               # 텍스트 객체의 출력 중심 좌표를 설정한다
                screen.blit(textSurfaceObj, textRectObj)

                screen.blit(self.nextblockbackground,(115,150))

                if self.NEXT_ITEM_SHOW_FLAG:

                    if self.bInstance.blockNextIndex==5:
                        for i in range(0,len(self.bInstance.nextBlock[0]),1):   # nextblock draw
                            for j in range(0,len(self.bInstance.nextBlock[0]),1):
                                if self.bInstance.nextBlock[0][i][j]==1:
                                    screen.blit(self.bInstance.blocksImage[self.tmpNextBlockColor],(115+(j*30),150+(i*30)))
                    elif self.bInstance.blockNextIndex==2:
                        for i in range(0,len(self.bInstance.nextBlock[0]),1):   # nextblock draw
                            for j in range(0,len(self.bInstance.nextBlock[0]),1):
                                if self.bInstance.nextBlock[0][i][j]==1:
                                    screen.blit(self.bInstance.blocksImage[self.tmpNextBlockColor],(145+(j*30),180+(i*30)))
                    else:
                        for i in range(0,len(self.bInstance.nextBlock[0]),1):   # nextblock draw
                            for j in range(0,len(self.bInstance.nextBlock[0]),1):
                                if self.bInstance.nextBlock[0][i][j]==1:
                                    screen.blit(self.bInstance.blocksImage[self.tmpNextBlockColor],(130+(j*30),165+(i*30)))

                itemBackgroundposition=[30,600]
                for i in range(0,6,1):
                    screen.blit(self.itemBackground,itemBackgroundposition)
                    itemBackgroundposition[0]+=50

                itemIconposition=[32,605]
                for i in range(0,len(self.itemQueue),1):
                    if self.itemQueue[i]==1:
                        screen.blit(self.itemIcon1,itemIconposition)
                    elif self.itemQueue[i]==2:
                        screen.blit(self.itemIcon2,itemIconposition)
                    elif self.itemQueue[i]==3:
                        screen.blit(self.itemIcon3,itemIconposition)
                    itemIconposition[0]+=50

                screen.blit(self.mInstance.img, self.mInstance.mapPosition)
                for i in range(2,self.mInstance.mapIndexSize[0]+2,1):    #draw block to map
                    for j in range(2,self.mInstance.mapIndexSize[1]+2,1):
                        if self.mInstance.mapData[i][j]!=0:
                            screen.blit(self.bInstance.blocksImage[self.mInstance.mapData[i][j]-1], (self.mInstance.mapPosition[0]+((j-2)*30),self.mInstance.mapPosition[1]+((i-2)*30)) )
                pygame.display.flip()  # 화면 전체를 업데이트
                self.clock.tick(self.TARGET_FPS)  # 프레임 수 맞추기
            else:
                if self.resetBlock():
                    return True
                else:
                    break
        return False

    def item1_removeBottomLine(self):  #맵에 블럭설치 이전에 호출할것
        self.eraseBlock()
        count=0
        for i in range(0,self.mInstance.mapIndexSize[1],1):
            if self.mInstance.mapData[self.mInstance.mapIndexSize[0]+1][i+2]!=0:
               count+=30
        self.mInstance.mapData.remove(self.mInstance.mapData[self.mInstance.mapIndexSize[0]+1])
        row=[]
        for j in range(0,self.mInstance.realMapIndexSize[1],1):
            row.append(0)
        row[1]=-1
        row[12]=-1
        self.mInstance.mapData.insert(0,row)
        self.gameScore+=count
        pass

    def item2_delayTime(self):
        self.DOWN_CYCLE_TIME+=0.2
        if self.DOWN_CYCLE_TIME>self.MAX_DOWN_CYCLE_TIME:
            self.DOWN_CYCLE_TIME=self.MAX_DOWN_CYCLE_TIME

        print ("delay speed, nowSpeed:",self.DOWN_CYCLE_TIME)
        pass

    def item3_showNextBlock(self):
        print ("next block:",self.bInstance.blockNextIndex)
        self.NEXT_ITEM_SHOW_FLAG=True
        self.tmpNextBlockColor=random.randrange(0,7)
        pass


    def gamePlay(self):
        print("gameplay")
        itemNum=0
        self.gameScore=0
        self.mInstance=map.Map()
        self.bInstance=block.Block()
        random.shuffle(self.itemQueue)
        screen = pygame.display.set_mode((700, 700), DOUBLEBUF)
        pygame.display.set_caption('Hello World!')  # 타이틀바의 텍스트를 설정

        screen.blit(pygame.image.load('./res/instruction.png'), (0, 0))#뒷배경
        pygame.display.flip()  # 화면 전체를 업데이트
        self.clock.tick(self.TARGET_FPS)  # 프레임 수 맞추기
        time.sleep(3)



        self.nowBlock=self.bInstance.reset()
        self.DOWN_START_TIME=time.time()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type== KEYDOWN:
                    if event.key==K_UP:
                        self.blockRotateUpdate()
                    if event.key==K_LCTRL:
                        print("ctrl")
                        if self.itemQueue:
                            itemNum=self.itemQueue.pop()
                            if itemNum==1:
                                self.item1_removeBottomLine()
                            elif itemNum==2:
                                self.item2_delayTime()
                            elif itemNum==3:
                                self.item3_showNextBlock()
                        else:
                            print("item empty")
                    if event.key==K_SPACE:
                        if self.blockSpaceBarUpdate(screen,self.background):
                            screen.blit(pygame.image.load('./res/gameover.png'), (0, 0))#뒷배경
                            pygame.display.flip()  # 화면 전체를 업데이트
                            self.clock.tick(self.TARGET_FPS)  # 프레임 수 맞추기
                            time.sleep(3)
                            return True
                        continue



            keyget=pygame.key.get_pressed()
            if keyget[K_DOWN]:
                self.blockDownUpdate()
                time.sleep(0.05)
            elif keyget[K_LEFT]:
                self.blockLeftUpdate()
                time.sleep(0.1)
            elif keyget[K_RIGHT]:
                self.blockRightUpdate()
                time.sleep(0.1)


            if time.time()-self.DOWN_START_TIME>=self.DOWN_CYCLE_TIME:
                self.DOWN_START_TIME=time.time()
                if not self.blockDownUpdate():
                    if self.isEndGame():
                        screen.blit(pygame.image.load('./res/gameover.png'), (0, 0))#뒷배경
                        pygame.display.flip()  # 화면 전체를 업데이트
                        self.clock.tick(self.TARGET_FPS)  # 프레임 수 맞추기
                        time.sleep(3)
                        return True
                    if self.resetBlock():
                        screen.blit(pygame.image.load('./res/gameover.png'), (0, 0))#뒷배경
                        pygame.display.flip()  # 화면 전체를 업데이트
                        self.clock.tick(self.TARGET_FPS)  # 프레임 수 맞추기
                        time.sleep(3)
                        return True


            self.insertBlock2Map()
            #self.mInstance.printMap()


            screen.blit(self.background, (0, 0))#뒷배경

            screen.blit(self.mInstance.img, self.mInstance.mapPosition)  #맵
            screen.blit(self.itemqueueBackground,(20,590))
            screen.blit(self.itemqueueBackground,(20,50)) # scoreboard

            fontObj = pygame.font.Font(None,32)                # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
            textSurfaceObj = fontObj.render(str(self.gameScore), True, (255,255,255))   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
            textRectObj = textSurfaceObj.get_rect();                      # 텍스트 객체의 출력 위치를 가져온다
            textRectObj.center = (175, 80)                               # 텍스트 객체의 출력 중심 좌표를 설정한다
            screen.blit(textSurfaceObj, textRectObj)

            screen.blit(self.nextblockbackground,(115,150))

            if self.NEXT_ITEM_SHOW_FLAG:

                if self.bInstance.blockNextIndex==5:
                    for i in range(0,len(self.bInstance.nextBlock[0]),1):   # nextblock draw
                        for j in range(0,len(self.bInstance.nextBlock[0]),1):
                            if self.bInstance.nextBlock[0][i][j]==1:
                                screen.blit(self.bInstance.blocksImage[self.tmpNextBlockColor],(115+(j*30),150+(i*30)))
                elif self.bInstance.blockNextIndex==2:
                    for i in range(0,len(self.bInstance.nextBlock[0]),1):   # nextblock draw
                        for j in range(0,len(self.bInstance.nextBlock[0]),1):
                            if self.bInstance.nextBlock[0][i][j]==1:
                                screen.blit(self.bInstance.blocksImage[self.tmpNextBlockColor],(145+(j*30),180+(i*30)))
                else:
                    for i in range(0,len(self.bInstance.nextBlock[0]),1):   # nextblock draw
                        for j in range(0,len(self.bInstance.nextBlock[0]),1):
                            if self.bInstance.nextBlock[0][i][j]==1:
                                screen.blit(self.bInstance.blocksImage[self.tmpNextBlockColor],(130+(j*30),165+(i*30)))



            itemBackgroundposition=[30,600]
            for i in range(0,6,1):
                screen.blit(self.itemBackground,itemBackgroundposition)
                itemBackgroundposition[0]+=50

            itemIconposition=[32,605]
            for i in range(0,len(self.itemQueue),1):
                if self.itemQueue[i]==1:
                    screen.blit(self.itemIcon1,itemIconposition)
                elif self.itemQueue[i]==2:
                    screen.blit(self.itemIcon2,itemIconposition)
                elif self.itemQueue[i]==3:
                    screen.blit(self.itemIcon3,itemIconposition)
                itemIconposition[0]+=50

            for i in range(0,self.mInstance.mapIndexSize[0],1):    #draw block to map
                for j in range(0,self.mInstance.mapIndexSize[1],1):
                    if self.mInstance.mapData[i+2][j+2]!=0:
                        screen.blit(self.bInstance.blocksImage[self.mInstance.mapData[i+2][j+2]-1], (self.mInstance.mapPosition[0]+(j*30),self.mInstance.mapPosition[1]+(i*30)) )
                        #print((self.mInstance.mapPosition[0]+((j-2)*30),self.mInstance.mapPosition[1]+((i-2)*30)))

            #self.mInstance.printMap()


            pygame.display.flip()  # 화면 전체를 업데이트
            self.clock.tick(self.TARGET_FPS)  # 프레임 수 맞추기
