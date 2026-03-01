import tkinter #used for visual frame
import random


class Frame():
    """allows for the visuals to run and be updated"""
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
    """holds all info for the map. Including wall locations and list of who is there"""
    width = 600
    height =600
    def __init__(self,c:tkinter.Canvas):
        self.canvas = c
        self.kids = list()
        self.elders = list()
        self.adults = list()
        self.sickList =list()
        self.walls = [[False for _ in range(600)] for _ in range(600)]
        self.sickArr = [[False for _ in range(600)] for _ in range(600)]
        self.gen_walls()
        self.madeHumans = False

    def tick(self):
        """allows for people to be moved with each tick"""
        allHumans = self.adults + self.kids + self.elders +self.sickList

        # Move all humans once
        for human in allHumans:
            human.move()

        # Spread sickness
        for human in allHumans:
            for i in range(human.getX() - 2, human.getX() + 2):
                for j in range(human.getY() - 2, human.getY() + 2):
                    if 0 <= i < 600 and 0 <= j < 600:
                        if (self.sickArr[i][j]) and (human.chanceIll()):
                            human.makesick()

        # Update sickArr for all sick humans
        for human in allHumans:
            if human.isSick:
                self.sickArr[human.getX()][human.getY()] = True        
        print("tick method")

    def draw (self):
        """called at start to make begening people """
        if self.madeHumans == False:
            self.madeHumans = True
            self.makeHumans()

    def makeHumans(self):
        """makes first humans """
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
        for i in range(1):
            H_point = self.safeLocation()
            x = H_point.getX()
            y = H_point.getY()
            h =Adults(self.canvas,x,y,self)
            h.makesick()
            self.sickList.append(h)
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
        
        def vert(midX,midY,baseW,baseH):
            #initialize to base value
            x = round(midX-.5*baseW)
            y = round(midY-.5*baseH)


            #initialize to base value
            w = round(x+ baseW)
            h = round(y+ baseH)


            self.canvas.create_rectangle(x, 0, w, 600,fill="black")
            for i in range(x, min(w, self.width)):
                for j in range(y, min(h, self.height)):
                    self.walls[i][j] = True

        def horiz(midX,midY,baseW,baseH):
            #initialize to base value
            x = round(midX-.5*baseW)
            y = round(midY-.5*baseH)


            #initialize to base value
            w = round(x+ baseW)
            h = round(y+ baseH)


            self.canvas.create_rectangle(0, y, 600, h,fill="black")
            for i in range(x, min(w, self.width)):
                for j in range(y, min(h, self.height)):
                    self.walls[i][j] = True


        
        def centerRoomPoints(midX,midY,baseW,baseH):
            #initialize to base value
            x = round(midX-.5*baseW)
            y = round(midY-.5*baseH)


            #initialize to base value
            w = round(x+ baseW)
            h = round(y+ baseH)


            self.canvas.create_rectangle(x, y, w, h,fill="black")
            for i in range(x, min(w, self.width)):
                for j in range(y, min(h, self.height)):
                    self.walls[i][j] = True

        def roomFromPoints(x,y,w,h):

            w+=x
            h+=y
            self.canvas.create_rectangle(x, y, w, h,fill="black")
            for i in range(x, min(w, self.width)):
                for j in range(y, min(h, self.height)):
                    self.walls[i][j] = True

        def findRoomLocation(w,h):
            
            x = random.randint(20,580)
            y = random.randint(20,580)
            
            for i in range(x, min(w+x+20, self.width)):
                for j in range(y, min(h+y+20, self.height)):
                    if (self.walls[i][j] == True):
                        return findRoomLocation(w,h)
            
            return Point(x,y)

        def placeRoom(w,h):
            start = findRoomLocation(w,h)
            roomFromPoints(start.getX(),start.getY(),w,h)

            midx = start.getX()+.5*w
            midy = start.getY()+.5*h

            horiz(midx,midy, 600,h/3)
            vert(midx,midy, w/3,600)
            

        #decide number of rooms to be generated

        rooms = random.randint(1,4)
        


        if rooms == 1:
            '''
            #OLD ALGORITHM

            #central room
            centerRoom(1/2,1/2,8/20,8/20)
            centerRoom(1/2,1/5,1/10,8/20,randY=0,randH=0,color='black')
            centerRoom(1/2,1/2,2,2/20,randX=0,randW=0,color='black')
            centerRoom(1/2,4/5,1/10,15/20,randY=0,randH=0,color='black')

            
            #borders
            randomRoom(0,0,1,2/20,rand=False)
            randomRoom(0,0,2/20,1,rand=False)
            randomRoom(18/20,0,2/20,1,rand=False)
            randomRoom(0,18/20,1,2/20,rand=False)
            '''

            #borders
            randomRoom(0,0,1,2/20,rand=False)
            randomRoom(0,0,2/20,1,rand=False)
            randomRoom(18/20,0,2/20,1,rand=False)
            randomRoom(0,18/20,1,2/20,rand=False)

            placeRoom(300,300)
        elif rooms ==2:
            #borders
            randomRoom(0,0,1,2/20,rand=False)
            randomRoom(0,0,2/20,1,rand=False)
            randomRoom(18/20,0,2/20,1,rand=False)
            randomRoom(0,18/20,1,2/20,rand=False)

            placeRoom(100,100)
            placeRoom(100,100)
        elif rooms ==3:
            #borders
            randomRoom(0,0,1,2/20,rand=False)
            randomRoom(0,0,2/20,1,rand=False)
            randomRoom(18/20,0,2/20,1,rand=False)
            randomRoom(0,18/20,1,2/20,rand=False)

            placeRoom(100,100)
            placeRoom(100,100)
            placeRoom(100,100)
        elif rooms ==4:
            #borders
            randomRoom(0,0,1,2/20,rand=False)
            randomRoom(0,0,2/20,1,rand=False)
            randomRoom(18/20,0,2/20,1,rand=False)
            randomRoom(0,18/20,1,2/20,rand=False)

            placeRoom(100,100)
            w = random.randint(50,100)
            placeRoom(w,w)
            placeRoom(100,100)
            w = random.randint(50,100)
            placeRoom(w,w)

        
        

        
        








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
        """find a safe location (in walkale area) where huamans are alllowed to be"""
        x = random.randint(0,580)
        y = random.randint(0,580)
        if self.walls[x][y] == False or self.walls[x+1][y+1] == False or self.walls[x+2][y+2] == False or self.walls[x+3][y+3] == False:
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
        self.isSick = False


    def move(self):
        """used to move all types of human - speed can be adjusted depending on what child is created """
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

        # Check wall collision  at new location
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

    #getter and setter
    def getdirction(self):
        return self.direction
    def setdirction(self,x):
        self.direction = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def makesick(self):
        self.isSick = True
        self.canvas.itemconfig(self.shape, fill='red')
    def chanceIll(self):
        if random.randint(0,100)<1:
            return True
        else:
            return False
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
        self.isSick = False
    def chanceIll(self):
        if random.randint(0,100)<2:
            return True
        else:
            return False
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
        self.isSick = False
    def chanceIll(self):
        if random.randint(0,100)<5:
            return True
        else:
            return False
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
    
#basic ui/splash
def click():

    Frame()

root = tkinter.Tk()
root.title("splash screen")
canvas = tkinter.Canvas(root, width=600, height=600, bg="#7dff13")
canvas.pack()

t = canvas.create_text(300, 40, text="Disease spreading simulation 🤒", font=("Helvetica", 20), fill="black")
t = canvas.create_text(300, 120, text="legend:", font=("Helvetica", 30,"bold"), fill="black")

s = canvas.create_rectangle(150, 150, 200, 200,fill="#a0a2eb")
t = canvas.create_text(250, 175, text="---> child", font=("Helvetica", 20), fill="black")

s = canvas.create_rectangle(150, 250, 200, 300,fill="#f55de8")
t = canvas.create_text(250, 275, text="---> elder", font=("Helvetica", 20), fill="black")

s = canvas.create_rectangle(150, 350, 200, 400,fill="yellow")
t = canvas.create_text(250, 375, text="---> adult", font=("Helvetica", 20), fill="black")

s = canvas.create_rectangle(150, 450, 200, 500,fill="red")
t = canvas.create_text(250, 475, text="---> sick", font=("Helvetica", 20), fill="black")

button = tkinter.Button (canvas,text='click here to start!',command=click)
button.place(x=240,y=60)
canvas.mainloop() 

