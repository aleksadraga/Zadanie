def setup():
    size(400, 400)
    textSize(30)
        
        
def draw():
    clear()
    background(200, 200, 200)
    fill(0, 150, 100)
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.vertex(300, 100)
    s.vertex(100, 100)
    s.vertex(130, 116)
    s.vertex(100, 200)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    text("A G", 180,160)
    
    if hex(get(mouseX, mouseY)) =='FF0000FF':
        fill(200, 0, 150)
        text("A G", 180, 160)
        
    print(keyPressed)
    if keyPressed:
        text("A", 180,160)
        if "A" == CODED:
            text("A", 180,160)
        fill(0,255,255)
        
        if keyPressed:
            if key=='a':
                text("A",180,160)
                a= fill (25,0,0)
        if keyPressed:
            if key=='g':
                text("G",210,160)
                g= fill(25,0,0)
