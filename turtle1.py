from telnetlib import FORWARD_X
import turtle as t

tim=t.turtles()

def draw_shapes(num_sides):
    angle= 360/ num_sides
    for _ in range (num_sides):
       

        for steps in range(100):
            for c in ('blue', 'red', 'green','orange'):
                tim.color(c)
                tim.forward(steps)

        draw_shapes(10)
    


