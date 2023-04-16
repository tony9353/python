smoothing = 3
penWidth = 10
penColor = [0, 0, 0]
def setup():
    size(1280, 720)
    background(255)

def draw():
    global penWidth, penColor
    strokeWeight(2)
    stroke(0)
    rect(1082, 2, 196, 716)
    rect(1087, 7, 88, 20)
    if mousePressed and cursorMode == "draw":
        pen()
    strokeWeight(penWidth)
    stroke(penColor[0], penColor[1], penColor[2])
    line(1132, 668, 1228, 668)

def pen():
    global x2, y2, smoothing, cursorMode, penWidth, penColor
    strokeWeight(penWidth)
    stroke(penColor[0], penColor[1], penColor[2])
    dx = mouseX - x2
    dy = mouseY - y2
    x1 = x2
    y1 = y2
    x2 += dx / smoothing
    y2 += dy / smoothing
    line(x1, y1, x2, y2)

def mousePressed():
    global x2, y2, cursorMode, penWidth, penColor
    if mouseX >= 1080:
        cursorMode = "side"
        if mouseX >= 1087 and mouseX <= 1175 and mouseY >= 7 and mouseY <= 27:
            penColor = [255, 255, 0]
    else:
        cursorMode = "draw"
        x2 = mouseX
        y2 = mouseY

def keyPressed():
    global penWidth, penColor
    print(key)
    if key == "0":
        background(255)
    elif key == "1":
        penColor = [0, 0, 0]
    elif key == "2":
        penColor = [255, 0, 0]
    elif key == "3":
        penColor = [0, 255, 0]
    elif key == "4":
        penColor = [0, 0, 255]
    elif key == "5":
        penColor = [255, 255, 0]
    elif key == "6":
        penColor = [255, 0, 255]
    elif key == "6":
        penColor = [0, 255, 255]
    elif key == "7":
        penColor = [255, 255, 255]
    elif key == "!":
        penWidth = 1
    elif key == "@":
        penWidth = 3
    elif key == "#":
        penWidth = 5
    elif key == "$":
        penWidth = 10
    elif key == "%":
        penWidth = 25
    elif key == "^":
        penWidth = 50