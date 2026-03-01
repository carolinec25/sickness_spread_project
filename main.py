import tkinter #used for visual frame
import random

class Frame():
    def __init__(self):
        w = 600
        h = 600

        self.root=tkinter.Tk()
        self.root.title("sickness")
        self.canvas = tkinter.Canvas(self.root,width=w,height=h,bg="white")
        self.hall = Hallway(self.canvas)
        self.canvas.pack()
        self.run() 
        self.root.mainloop()
    def run(self):
        #self.hall.tick()
        #self.hall.draw()
        self.root.after(20,self.run)
class Hallway():
    width = 600
    height= 600
    #assign colors
    KRGB = "blue"
    ERGB = "green"
    ARGB = "yellow"
    #need do 
    
    def __init__(self,canvas):
        self.canvas = canvas
        kids = list()
        elders = list()
        adults = list()
        self.walls = [[False for _ in range(self.height)] for _ in range(self.width)]
        self.gen_walls()
        self.madeHumans = False
    def tick(self):
        pass
    def draw (self):
        def makeHumans():
            for i in range(5000):
                pass
                #need to set direction
        if self.madeHumans == False:
            madeHumans = True

    def gen_walls(self):
        
        def randomRoom(baseX,baseY,baseW,baseH,
                       randX=1/10,randY=1/10,randW=3/20,randH=3/20,color = "black"):
            #initialize to base value
            x = round(baseX*self.width)
            y = round(baseY*self.height)

            #add/subtract random amounts
            x+= random.randint(round(-randX*self.width), round(randY*self.width))
            y+= random.randint(round(-randX*self.height), round(randY*self.height))

            #initialize to base value
            w = round(x+ baseW*self.width)
            h = round(y+ baseH*self.height)

            #add/subtract random amounts
            w+= random.randint(0,round(randW*self.width))
            h+= random.randint(0,round(randH*self.height))

            self.canvas.create_rectangle(x, y, w, h,fill=color)
            for i in range(x, min(x, self.width)):
                for j in range(y, min(y, self.height)):
                    self.walls[i][j] = True
        
        def centerRoom(midX,midY,baseW,baseH,
                       randX=1/10,randY=1/10,randW=3/20,randH=3/20,color = "black"):
            #initialize to base value
            x = round(midX*self.width-.5*baseW*self.height)
            y = round(midY*self.height-.5*baseH*self.height)

            #add/subtract random amounts
            x+= random.randint(round(-randX*self.width), round(randY*self.width))
            y+= random.randint(round(-randX*self.height), round(randY*self.height))

            #initialize to base value
            w = round(x+ baseW*self.width)
            h = round(y+ baseH*self.height)

            #add/subtract random amounts
            w+= random.randint(0,round(randW*self.width))
            h+= random.randint(0,round(randH*self.height))

            self.canvas.create_rectangle(x, y, w, h,fill=color)
            for i in range(x, min(x, self.width)):
                for j in range(y, min(y, self.height)):
                    self.walls[i][j] = True

        #central room
        randomRoom(7/20,7/20,5/20,5/20)
        #randomRoom(1/20,15/20,3/20,1/20)
        centerRoom(1/2,1/5,1/10,15/20,randY=0,randH=0,color='blue')
        centerRoom(1/2,1/2,2,2/20,randX=0,randW=0,color='blue')
        centerRoom(1/2,4/5,1/10,15/20,randY=0,randH=0,color='blue')
        








        '''
        for V in range(50): #makes rooms
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            w = random.randint(20, 60)
            h = random.randint(20, 40)
            self.canvas.create_rectangle(x, y, x+h, y+w,fill="black")
            for i in range(x, min(x+w, 600)):
                for j in range(y, min(y+h, 600)):
                    self.walls[i][j] = True

        for V in range(100): #makes halls
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            w = random.randint(10, 140)
            h = random.randint(10,100)
            self.canvas.create_rectangle(x, y, x+w, y+h,fill="black")
            for i in range(x, min(x+w, 600)):
                for j in range(y, min(y+h, 600)):
                    self.walls[i][j] = True
        self.canvas.create_rectangle(x, y, 299, 299,fill="black")
        '''
    def safeLocation(self):
        pass
class Humans():
     pass
""" class Children(humans):
     pass
class Edlers(humans):
     pass
class Adults(humans):
     pass """
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
Frame()
