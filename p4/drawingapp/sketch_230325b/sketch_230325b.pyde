def setup():
    size(1280, 720)
    background(255)
    lastMouseX = mouseX
    lastMouseY = mouseY

def draw():
    strokeWeight(10)
    ellipse(mouseX, mouseY, 10, 10)
    #line(mouseX, mouseY, lastMouseX, lastMouseY)
    #lastMouseX = mouseX
    #lastMouseY = mouseY
def keyPressed():
    print(f"key: {key}")
    print(f"ord: {ord('r')}")
    if key == ord("r"):
        background(255)