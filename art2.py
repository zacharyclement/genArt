from generativepy import drawing
from generativepy.drawing import makeImage
from generativepy.color import Color
import math
import random

N = 400

colors = [
    Color('white'),
    #Color('black'),
    #Color('lightgray'),
    #Color('darkgray'),
    #Color('lightgray'),
    ]

def draw(canvas):
    color = random.choice(colors)
    points = [(math.cos(i*2*math.pi/N), math.sin(i*2*math.pi/N)) for i in range(N)]
    canvas.stroke(color)
    canvas.strokeWeight(0.005)

    for i in range(N):  #[1,2,3,4,5...]
        print('i = ', i)
        j = (i*15) % N
        print('j= ', j)
        print('unpack i: ', *points[i], ' unpack j: ', *points[j])
        canvas.line(*points[i], *points[j])

makeImage("circles.png", draw, pixelSize=(800, 800), width=2.2,
          startX=-1.1, startY=-1.1, background=Color(0.25))
