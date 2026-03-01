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
    height= 600
    #assign colors
    KRGB = "blue"
    ERGB = "green"
    ARGB = "yellow"
    #need do 
    
    def __init__(self,canvas):
        self.canvas = canvas
        self.kids = list()
        self.elders = list()
        self.adults = list()
        self.walls = [[False for _ in range(self.height)] for _ in range(self.width)]
        self.gen_walls()
        self.madeHumans = False

    def tick(self):
        for a in self.adults:
            a.move()
        print("tick method")

    def draw (self):
        if self.madeHumans == False:
            self.madeHumans = True
            self.makeHumans()

    def makeHumans(self):
        for i in range(500):
            H_point = self.safeLocation()
            x = H_point.getX()
            y = H_point.getY()
            h = Humans(self.canvas,x,y,self)
            self.adults.append(h)
            #need to set direction
    def getAdultList(self):
        return self.adults
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
            for i in range(x, min(x+w, self.width)):
                for j in range(y, min(y+h, self.height)):
                    self.walls[i][j] = True

        #central room
        randomRoom(7/20,7/20,5/20,5/20)
        randomRoom(1/20,15/20,3/20,1/20)








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
        self.shape = self.canvas.create_rectangle(x, y, x+4, y+4, fill="red")
        self.direction = random.randint(0,3)
        self.h =h

    def move(self):
        dx, dy = 0, 0

        if self.direction == 0:
           dy = -2
        elif self.direction == 1:
           dy = 2
        elif self.direction == 2:
            dx = -2
        elif self.direction == 3:
            dx = 2

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
                    

        # If no collision, move
        self.canvas.move(self.shape, dx, dy)
        self.x = new_x
        self.y = new_y
        if random.random() < 0.02:
            self.direction = random.randint(0,3)
        
    def getdirction(self):
        return self.direction
    def setdirction(self,x):
        self.direction = x

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
