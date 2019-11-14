# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    def presscolor(self,randcolor):
        self.c=randcolor
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
#3-1    
myCar1 = Car(color(255, 255, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)


#I changed the color of myCar2 to yellow just to see what happens. I need to figure out how to randomize something.
# I added the random function to the code.
#It failed because I initially kept all three aspects of the color. Got a error message because random can only have 1 or 2 arguments.
#after I changed it to range random(255) and fixed parenthesis balance issues, it worked.
#The color changes every time the program is run.
#There were some issues with indenting initially. For example, else: autoindented after the keypress function.
#Fixed that, but now it says 'keyPressed' is not defined.
#Fair. Guess I have to define it.
#Wait. Looking on the internet beyond the given tutorial, it says keyPress in no longer relevant and to use keyCode instead.
#This works, but it doesn't actually call the random code. I removed "space bar" and tried it with "A".
#Still didn't work.
#This stops working when the keyPress code is added. It works when that code isn't there.
#very annoying.
def setup():
    size(200,200)
    if ((keyCode) and (key == ' ')):
        myCar1=Car(color(random(255)), 0, 100, 2)

#There was an error here. Line 26 needed to be indented.
#3-2
def setup(): 
    size(200, 200)
    print("test")
    
#3-3
class froggo(object):

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
            
class froggo(object):

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
myfroggo1 = froggo(color(255, 144, 133), random(0,200), random(0,200), 3)
myfroggo2 = froggo(color(0, 255, 130), random(0,200), random(0,200), 13)
myfroggo3 = froggo(color(1, 144, 133), random(0,200), random(0,200),10)
myfroggo4 = froggo(color(22, 255, 130), random(0,200), random(0,200), 1)

            
class rock(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed

    def movearound (self, xpos, ypos):
        self.xpos=xpos
        self.ypos=ypos
        
        
    def display(self):
        stroke(0)
        fill(self.c)
        ellipseMode(CENTER)
        ellipse(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
myrock1= rock(color(22,55,155), 0, 0, 2)
def mousePressed():
   myrock1.movearound(mouseX, mouseY) 

     
myrock1 = rock(color(0, 144, 133), 0, 0, 3)

class magicstump(object):

    def __init__(self, c, xpos, ypos):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos

    def display(self):
        stroke(0)
        fill(self.c)
        ellipseMode(CENTER)
        ellipse(self.xpos, self.ypos, 25, 30);
        
    def changeshape(self, c, xpos, ypos):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 25, 30);
    
        
mymagicstump1 = magicstump(color(50, 144, 255), 100, 100)
    
def setup():
    size(400,200)
    noStroke()
    
def words():
    str('Press 1 for magic stump~')
    

 #I tried using key code t   
def draw(): 
  background(255)
  words()
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
  if (keyPressed) and (key==' '):
    myCar2.presscolor(color(random(255)))
  myfroggo1.drive()
  myfroggo1.display()
  myfroggo2.drive()
  myfroggo2.display()
  myfroggo3.drive()
  myfroggo3.display()
  myfroggo4.drive()
  myfroggo4.display()
  myrock1.display()
  mymagicstump1.display()
  if (keyPressed) and (key=='1'):
     mymagicstump1.changeshape(color(50, 144, 255), 100, 100)
  textSize(20)
  text('Press 1 for magic stump~', 15, 15)
     
  



#I changed a number of the parameters from the Car example given, and renamed it to froggo.
#I gave the frogs a variety of green shade, but for one.
#Because I thought the coral was cute.
#I also changed where they appeared in their neat little frog race.
#And gave them different speeds. 
#Some frogs just weren't feeling this race and move slowly.
#I tried to move this function to the end of the code to see if that was an issue. 
#Apparently not.
