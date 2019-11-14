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
    
myfroggo1 = froggo(color(255, 144, 133), 0, 150, 3)
myfroggo2 = froggo(color(0, 255, 130), 0, 50, 13)
myfroggo3 = froggo(color(1, 144, 133), 0, 80,10)
myfroggo4 = froggo(color(22, 255, 130), 0, 5, 1)
    
def setup():
    size(200,200)

def draw(): 
  background(255)
  myfroggo1.drive()
  myfroggo1.display()
  myfroggo2.drive()
  myfroggo2.display()
  myfroggo3.drive()
  myfroggo3.display()
  myfroggo4.drive()
  myfroggo4.display()
#I changed a number of the parameters from the Car example given, and renamed it to froggo.
#I gave the frogs a variety of green shade, but for one.
#Because I thought the coral was cute.
#I also changed where they appeared in their neat little frog race.
#And gave them different speeds. 
#Some frogs just weren't feeling this race and move slowly.
