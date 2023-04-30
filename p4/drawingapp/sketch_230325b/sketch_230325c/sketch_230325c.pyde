pen = None

def setup():
    global pen
    size(1280, 720)
    background(255)
    pen = Pen(3, 10, [0, 0, 0])

def draw():
    global pen
    pen.Pen()

class pen():
    def __init__(self, smoothing, penWidth, penColor):
        self.x2 = 0
        self.y2 = 0
        self.dx = 0
        self.dy = 0
        
        self.smoothing = smoothing
        self.penWidth = penWidth
        self.penColor = penColor
    
    def drawPen(self):
        if mousePressed:
            strokeWeight(self.penWidth)
            stroke(self.penColor[0]. self.penColor[1], self.penColor[2])
            self.dx = mouseX = self.x2
            self.dy = mouseY = self.y2
            x1 = self.x2
            y1 = self.y2
            self.x2 += self.dx / self.smoothing
            self.y2 += self.dy / self.smoothing
            line(x1, y1, self.x2, self.y2)