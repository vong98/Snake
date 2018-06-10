class Snake():
    SIZE = 25
    facing = [x, y] = [1, 0]
    headX = 200
    headY = 300

def face(x, y):
        Snake.facing[0] = x
        Snake.facing[1] = y
        print("x: " + Snake.facing[0].__str__())
        print("Y: " + Snake.facing[1].__str__())

def move():
    Snake.headX = Snake.headX + Snake.facing[0]*Snake.SIZE
    Snake.headY = Snake.headY + Snake.facing[1]*Snake.SIZE
    
def getSize():
    return Snake.SIZE

def getX():
    return Snake.headX

def getY():
    return Snake.headY
