from microbit import *

# led Snake 
py = 0
lista: List[number] = []
dy = 0
for px in range(5):
    for indeks in range(5):
        py = abs(dy - indeks)
        led.plot(px, py)
        basic.pause(200)
        lista.unshift(px)
        lista.unshift(py)
        if len(lista) >= 5:
            led.unplot(lista.pop(), lista.pop())
    dy = 4 - dy