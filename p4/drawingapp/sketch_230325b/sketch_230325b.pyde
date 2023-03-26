def setup():
    size(1280, 720)
    background(100)
    lastMouseX = mouseX
    lastMouseY = mouseY

def draw():
    strokeWeight(10)
    stroke
    line(mouseX, mouseY, lastMouseX, lastMouseY)
    lastMouseX = mouseX
    lastMouseY = mouseY
