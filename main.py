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
        self.sicklist = list()
        self.walls = [[False for _ in range(600)] for _ in range(600)]
        self.sickArr = [[False for _ in range(600)] for _ in range(600)]
        self.gen_walls()
        self.madeHumans = False

    def tick(self):
        for i in range(len(self.adults)-1):
            a=self.adults[i]
            a.move()
            for i in range(a.getX(), a.getX() + 5):
                for j in range(a.getY(), a.getY() +5):
                    if self.sickArr[a.getX()][a.getY()]== True:
                        ill = sick(a.getcanvas(),a.getX(),a.getY(),self)
                        self.sicklist.append(ill)
                        del self.adults[i]
        for c in self.kids:
            c.move()   
        for e in self.elders:
            e.move()       
        for s in self.sicklist:
            s.move()      
            self.sickArr[s.getX()][s.getY()] = True 
   
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
        for i in range(3):
            H_point = self.safeLocation()
            x = H_point.getX()
            y = H_point.getY()
            self.sickArr[x][y] = True
            h = sick(self.canvas,x,y,self)
            self.sicklist.append(h)
            #need to set direction
    def getAdultList(self):
        return self.adults
    def gen_walls(self):
        self.canvas.create_rectangle(0, 0, 600, 600,fill="white",width=0)
        for V in range(50): #makes rooms
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            w = random.randint(20, 60)
            h = random.randint(20, 40)
            self.canvas.create_rectangle(x, y, x+h, y+w,fill="#d4c4a1",width=0)
            for i in range(x, min(x+w, 600)):
                for j in range(y, min(y+h, 600)):
                    self.walls[i][j] = True

        for V in range(100): #makes halls
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            w = random.randint(10, 140)
            h = random.randint(10,100)
            self.canvas.create_rectangle(x, y, x+w, y+h,fill="#d4c4a1",width=0)
            for i in range(x, min(x+w, 600)):
                for j in range(y, min(y+h, 600)):
                    self.walls[i][j] = True
        self.canvas.create_rectangle(x, y, 299, 299,fill="#d4c4a1",width=0)
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
        self.range = 10

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

    def getcanvas(self):
        return self.canvas
    def getdirction(self):
        return self.direction
    def setdirction(self,x):
        self.direction = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y
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
    
class sick(Humans):
    def __init__(self, canvas, x, y,h):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 4
        self.shape = self.canvas.create_rectangle(x, y, x+4, y+4, fill="red")
        self.direction = random.randint(0,3)
        self.h =h
        self.speed = 1
        self.rFactor = 10

    pass
Frame()
