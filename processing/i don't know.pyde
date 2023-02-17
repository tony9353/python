from random import randint
Car1 = None
Car2 = None
Car3 = None
bgr = randint(0, 255)
bgg = randint(0, 255)
bgb = randint(0, 255)

def setup():
    global Car1, Car2, Car3
    size(512, 512)
    Car1 = Car(256, 256, 2, 190, 0, randint(0, 255), randint(0, 255), randint(0, 255))
    Car2 = Car(256, 256, 1, 150, 0, randint(0, 255), randint(0, 255), randint(0, 255))
def draw():
    global Car1, Car2, bgr, bgg, bgb
    background(bgr, bgg, bgb)
    fill(0)
    Car1.display()
    Car2.display()
    Car1.drive()
    Car2.drive()
    
class Car:
    def __init__(self, x, y, dx, dy, rotation, r, g, b):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotation = rotation
        self.r = r
        self.g = g
        self.b = b
    
    def display(self):
        stroke(self.r, self.g, self.b)
        fill(self.r, self.g, self.b)
        translate(self.x, self.y + round(sin(self.rotation * PI / 180) * self.dy))
        rotate(self.rotation * PI / 180)
        rectMode(CENTER)
        ellipse(0, 0, 50, 50)
        fill(255)
        ellipse(-12, -10, 10, 10)
        ellipse(12, -10, 10, 10)
        rect(0, 15, 20, 5)
    
    def drive(self):
        self.x += self.dx #x
        if self.x > width + 50:
            self.x = -50
        self.rotation += self.dx # rotation
        if self.rotation > 360:
            self.rotation = 1
