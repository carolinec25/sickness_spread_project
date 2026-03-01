import tkinter #used for visual frame
import random

class Frame():
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("sickness")
        self.canvas = tkinter.Canvas(self.root,width=600,height=600,bg="white")
        self.hall = Hallway(self.canvas)
        self.canvas.pack()
        #self.walls = [[False for _ in range(self.HEIGHT)] for _ in range(self.WIDTH)]
        self.run() 
        self.root.mainloop()
    def run(self):
        #self.hall.tick()
        #self.hall.draw()
        self.root.after(20,self.run)
class Hallway():
    width = 600
    height =600
    #assighn colors
    KRGB = "blue"
    ERGB = "green"
    ARGB = "yellow"
    #need do 
    
    def __init__(self,canvas):
        self.canvas = canvas
        kids = list()
        elders = list()
        adults = list()
        self.walls = [[False for _ in range(600)] for _ in range(600)]
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
        self.canvas.create_rectangle(0, 0, 600, 600,fill="white")
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
