import pygame

class Map:
    mapPosition=(350,50)
    mapSize=(300,600)
    img=''
    mapIndexSize=(20,10)
    realMapIndexSize=(24,14)
    def __init__(self):
        self.mapData=[]
        self.img=pygame.image.load('./res/map.png')

        self.initMap()
        #self.printMap()
        pass


    def initMap(self):
        for i in range(0,self.realMapIndexSize[0],1):
            row=[]
            if i==self.realMapIndexSize[0]-2:
                for j in range(0,self.realMapIndexSize[1],1):
                    row.append(-1)
            else:
                for j in range(0,self.realMapIndexSize[1],1):
                    row.append(0)
            row[1]=-1
            row[12]=-1
            self.mapData.append(row)

    def printMap(self):
        for i in range(0,self.realMapIndexSize[0],1):
            if i<self.realMapIndexSize[1]:
                print(i,"  ",end="")
            else:
                print(i," ",end="")

            for j in range(0,self.realMapIndexSize[1],1):
                print(self.mapData[i][j],end="")
            print("")

    def __del__(self):
        pass

    def scoreCheck(self):
        deleteLine=0
        for i in range(2,self.mapIndexSize[0]+2,1):
            count=0
            for j in range(2,self.mapIndexSize[1]+2,1):
                if self.mapData[i][j]!=0:
                    count+=1
            if count==10:
                self.mapData.remove(self.mapData[i])
                deleteLine+=1
                row=[]
                for j in range(0,self.realMapIndexSize[1],1):
                    row.append(0)
                row[1]=-1
                row[12]=-1
                self.mapData.insert(0,row)
        return deleteLine
