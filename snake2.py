def hideTail():
    if len(snakeList) > 6:
        led.unplot(snakeList.pop(), snakeList.pop())
def outOfScreen(num: number):
    if num < 0 or num > 4:
        return 1
    else:
        return 0
def moveHead():
    global px, dx, py, dy
    if direction == HORIZONTAL:
        px += dx
        if outOfScreen(px) == 1:
            dx = dx * -1
            px += dx
            py += dy
    else:
        py += dy
        if outOfScreen(py) == 1:
            dy = dy * -1
            py += dy
            px += dx
def showHead():
    led.plot(px, py)
    snakeList.unshift(px)
    snakeList.unshift(py)
def switchDirection():
    global direction
    if direction == HORIZONTAL:
        direction = VERTICAL
    else:
        direction = HORIZONTAL
def escapeOuterCorner():
    global dy, py, dx, px
    if outOfScreen(py) == 1:
        dy = dy * -1
        py += dy
        switchDirection()
        moveHead()
    if outOfScreen(px) == 1:
        dx = dx * -1
        px += dx
        switchDirection()
        moveHead()
dy = 0
dx = 0
direction = 0
VERTICAL = 0
HORIZONTAL = 0
snakeList: List[number] = []
py = 0
px = 0
basic.clear_screen()
px = 0
py = 0
snakeList = []
HORIZONTAL = 111
VERTICAL = 222
direction = HORIZONTAL
dx = 1
dy = 1

def on_forever():
    showHead()
    basic.pause(200)
    hideTail()
    moveHead()
    escapeOuterCorner()
    
basic.forever(on_forever)
