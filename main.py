import tkinter #used for visual frame
import random
import time

class Frame():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("sickness")

        self.canvas = tkinter.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.hall = Hallway(self.canvas)

        self.run()
        self.root.mainloop()   

    def run(self):
        self.hall.draw()
        self.hall.tick()
        self.root.after(20, self.run)
    



class Hallway():
    width = 600
    height =600
    def __init__(self,c:tkinter.Canvas):
        self.canvas = c
        self.kids = list()
        self.elders = list()
        self.adults = list()
        self.walls = [[False for _ in range(600)] for _ in range(600)]
        self.gen_walls()
        self.madeHumans = False

    def tick(self):
        for a in self.adults:
            a.move()
        for c in self.kids:
            c.move()   
        for e in self.elders:
            e.move()              
        print("tick method")

    def draw (self):
        if self.madeHumans == False:
            self.madeHumans = True
            self.makeHumans()

    def makeHumans(self):
        for i in range(400):
            H_point = self.safeLocation()
            x = H_point.getX()
            y = H_point.getY()
            h = Adults(self.canvas,x,y,self)
            self.adults.append(h)
        for i in range(400):
            H_point = self.safeLocation()
            x = H_point.getX()
            y = H_point.getY()
            h = Children(self.canvas,x,y,self)
            self.kids.append(h)
        for i in range(200):
            H_point = self.safeLocation()
            x = H_point.getX()
            y = H_point.getY()
            h = Edlers(self.canvas,x,y,self)
            self.elders.append(h)
            #need to set direction
    def getAdultList(self):
        return self.adults
    def gen_walls(self):
        
        def randomRoom(baseX,baseY,baseW,baseH,
                       randX=1/10,randY=1/10,randW=3/20,randH=3/20,color = "black",rand=True):
            #initialize to base value
            x = round(baseX*self.width)
            y = round(baseY*self.height)

            if (rand):
                #add/subtract random amounts
                x+= random.randint(round(-randX*self.width), round(randY*self.width))
                y+= random.randint(round(-randX*self.height), round(randY*self.height))

            #initialize to base value
            w = round(x+ baseW*self.width)
            h = round(y+ baseH*self.height)

            if (rand):
                #add/subtract random amounts
                w+= random.randint(0,round(randW*self.width))
                h+= random.randint(0,round(randH*self.height))

            self.canvas.create_rectangle(x, y, w, h,fill=color)
            for i in range(x, min(w, self.width)):
                for j in range(y, min(h, self.height)):
                    self.walls[i][j] = True
        
        def centerRoom(midX,midY,baseW,baseH,
                       randX=1/10,randY=1/10,randW=3/20,randH=3/20,color = "black",
                       rand = True):
            #initialize to base value
            x = round(midX*self.width-.5*baseW*self.height)
            y = round(midY*self.height-.5*baseH*self.height)

            if (rand):
                #add/subtract random amounts
                x+= random.randint(round(-randX*self.width), round(randY*self.width))
                y+= random.randint(round(-randX*self.height), round(randY*self.height))

            #initialize to base value
            w = round(x+ baseW*self.width)
            h = round(y+ baseH*self.height)

            if (rand):
                #add/subtract random amounts
                w+= random.randint(0,round(randW*self.width))
                h+= random.randint(0,round(randH*self.height))

            self.canvas.create_rectangle(x, y, w, h,fill=color)
            for i in range(x, min(w, self.width)):
                for j in range(y, min(h, self.height)):
                    self.walls[i][j] = True
        
        #central room
        centerRoom(1/2,1/2,8/20,8/20)
        centerRoom(1/2,1/5,1/10,11/20,randY=0,randH=0,color='black')
        centerRoom(1/2,1/2,2,2/20,randX=0,randW=0,color='black')
        centerRoom(1/2,4/5,1/10,15/20,randY=0,randH=0,color='black')

        
        #borders
        randomRoom(0,0,1,2/20,rand=False)
        randomRoom(0,0,2/20,1,rand=False)
        randomRoom(18/20,0,2/20,1,rand=False)
        randomRoom(0,18/20,1,2/20,rand=False)
        
        
    








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
        x = random.randint(0,580)
        y = random.randint(0,580)
        if self.walls[x][y] == False:
            return self.safeLocation()
        else:
            return Point(x,y)
    def getHalls(self):
        return self.walls
        

class Humans():
    def __init__(self, canvas, x, y,h):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 4
        self.shape = self.canvas.create_rectangle(x, y, x+4, y+4, fill="yellow")
        self.direction = random.randint(0,3)
        self.h =h
        self.speed = 2
        self.rFactor = 10


    def move(self):
        dx, dy = 0, 0

        if self.direction == 0:
           dy = -self.speed
        elif self.direction == 1:
           dy = self.speed
        elif self.direction == 2:
            dx = -self.speed
        elif self.direction == 3:
            dx = self.speed

        new_x = self.x + dx
        new_y = self.y + dy

        # Check screen bounds first
        if not (0 <= new_x <= 596 and 0 <= new_y <= 596):
            self.direction = random.randint(0,3)
            return

        # Check wall collision ONLY at new location
        for i in range(new_x, new_x + self.size):
            for j in range(new_y, new_y + self.size):
                if self.h.walls[i][j] == False:
                    self.direction = random.randint(0,3)
                    return
        r = random.randint(0,100)
        if r<self.rFactor:
             self.direction = random.randint(0,3)
        # If no collision, move
        self.canvas.move(self.shape, dx, dy)
        self.x = new_x
        self.y = new_y

       
    def getdirction(self):
        return self.direction
    def setdirction(self,x):
        self.direction = x

class Children(Humans):
    def __init__(self, canvas, x, y,h):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 4
        self.shape = self.canvas.create_rectangle(x, y, x+4, y+4, fill="#a0a2eb")
        self.direction = random.randint(0,3)
        self.h =h
        self.speed = 3
        self.rFactor = 30
    pass
class Edlers(Humans):
    def __init__(self, canvas, x, y,h):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 4
        self.shape = self.canvas.create_rectangle(x, y, x+4, y+4, fill="#f55de8")
        self.direction = random.randint(0,3)
        self.h =h
        self.speed = 1
        self.rFactor = 10
    pass
class Adults(Humans):
     pass 



class Point():
    def __init__(self,x,y):
        self.x = x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
Frame()
