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
class squiggleline(object):
    c=color(255)
    
def draw():
    frameRate(5)
    println(pmouseX - mouseX)
    
def setup():
    size(200, 200)
    strokeWeight(8)


def draw():
    line(mouseX, mouseY, pmouseX, pmouseY)
#3-4    
#Not sure if all of this is supposed to be in the same code, but I'm completing the tasks.
#I named the class squiggle and set the color to black?
#I think?
#I made a draw function that creates a line that stays written on the background.
#Orginally, the background autorefreshed so the lines wouldn't stay. Removing this piece of code makes the drawing stay.
#Now the line stays. 
#I also changed the frame rate, size and stroke weight to something managable.
#3-5
#I haven't been able to make more than one element run at once. 
#I think part of this has to do with some updates to python. For example, the keyPress code didn't work and I had to find a different one online.
#I think in theory, that if we didn't redefine the draw function each time, the code would stay visible.
#But I'm not how to do this, since draw is a set function in processing. I think it's like print?
