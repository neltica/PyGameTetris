import random
import pygame

class Block:

    RED=1
    ORANGE=2
    YELLOW=3
    GREEN=4
    SKY=5
    BLUE=6
    PURPLE=7

    blocksCount=7
    blockNextIndex=0
    blockIndex=0
    blockRotate=0
    blockColor=''
    startPos=(2,6)
    nowPos=[]
    nowBlock=[]
    nextBlock=[]

    blockMoveTime=0

    def __init__(self):
        self.blockS=[]
        self.blockZ=[]
        self.blockB=[]
        self.blockJ=[]
        self.blockL=[]
        self.blockT=[]
        self.blockI=[]
        self.blocksImage=[]

        self.blocksData=[self.blockS,self.blockZ,self.blockB,self.blockJ,self.blockL,self.blockI,self.blockT]
        self.initBlocks()
        pass

    def initBlocks(self):
        self.blockS.append([[0,1,1],[1,1,0],[0,0,0]])
        self.blockS.append([[0,1,0],[0,1,1],[0,0,1]])
        self.blockS.append([[0,0,0],[0,1,1],[1,1,0]])
        self.blockS.append([[1,0,0],[1,1,0],[0,1,0]])

        self.blockZ.append([[1,1,0],[0,1,1],[0,0,0]])
        self.blockZ.append([[0,0,1],[0,1,1],[0,1,0]])
        self.blockZ.append([[0,0,0],[1,1,0],[0,1,1]])
        self.blockZ.append([[0,1,0],[1,1,0],[1,0,0]])

        self.blockB.append([[1,1],[1,1]])

        self.blockJ.append([[1,0,0],[1,1,1],[0,0,0]])
        self.blockJ.append([[0,1,1],[0,1,0],[0,1,0]])
        self.blockJ.append([[0,0,0],[1,1,1],[0,0,1]])
        self.blockJ.append([[0,1,0],[0,1,0],[1,1,0]])

        self.blockL.append([[0,0,1],[1,1,1],[0,0,0]])
        self.blockL.append([[0,1,0],[0,1,0],[0,1,1]])
        self.blockL.append([[0,0,0],[1,1,1],[1,0,0]])
        self.blockL.append([[1,1,0],[0,1,0],[0,1,0]])

        self.blockI.append([[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]])
        self.blockI.append([[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]])
        self.blockI.append([[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]])
        self.blockI.append([[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]])

        self.blockT.append([[0,1,0],[1,1,1],[0,0,0]])
        self.blockT.append([[0,1,0],[0,1,1],[0,1,0]])
        self.blockT.append([[0,0,0],[1,1,1],[0,1,0]])
        self.blockT.append([[0,1,0],[1,1,0],[0,1,0]])

        self.blocksImage.append(pygame.image.load('./res/r.png'))
        self.blocksImage.append(pygame.image.load('./res/o.png'))
        self.blocksImage.append(pygame.image.load('./res/y.png'))
        self.blocksImage.append(pygame.image.load('./res/g.png'))
        self.blocksImage.append(pygame.image.load('./res/s.png'))
        self.blocksImage.append(pygame.image.load('./res/b.png'))
        self.blocksImage.append(pygame.image.load('./res/p.png'))
        self.blockNextIndex=random.randrange(0,self.blocksCount)
        self.nextBlock=self.blocksData[self.blockNextIndex]


    def __del__(self):
        pass

    def reset(self):
        self.nowPos=list(self.startPos)
        self.blockIndex=self.blockNextIndex
        self.blockNextIndex=random.randrange(0,self.blocksCount)
        self.blockColor=random.randrange(0,self.blocksCount)

        self.nowBlock=self.blocksData[self.blockIndex]
        self.nextBlock=self.blocksData[self.blockNextIndex]
        self.blockRotate=0
        print("resetblock")
        print("blockIndex:",self.blockIndex)
        print("blockColor:",self.blockColor)
        print("nowBlock:",self.nowBlock)
        return self.blocksData[self.blockIndex]
