from turtle import *


def triangle():
    forward(120)
    left(120)
    forward(120)
    left(120)
    forward(120)

for steps in range(100):
    for c in ('blue', 'red', 'green','orange'):
        color(c)
        forward(steps)
        right(45)
        
        width(3)
        speed(1000)
        