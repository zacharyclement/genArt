from generativepy import drawing
from generativepy.drawing import Color, ROUND
from scipy.spatial import Delaunay
import random

SIZE = 1000

colors = [
    Color('white'),
    #Color('black'),
    #Color('lightgray'),
    #Color('darkgray'),
    #Color('lightgray'),
    ]

def triangle(canvas, a, b, c):
    color = random.choice(colors)
    canvas.fill(color)
    canvas.stroke(Color('black'))
    canvas.strokeWeight(1)
    canvas.triangle(*a, *b, *c)


def draw(canvas):
    #random.seed(30)
    #randrange([start,] stop [,step])
    centerFactor = .25
    x_cord = (random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))))
    y_cord = (random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))))
    
    
    points = [(random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))), random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))))
               for i in range(100)]

    #points = [(x_cord, y_cord)
    #           for i in range(1000)]
    
    tri = Delaunay(points)
    for a, b, c in tri.simplices:
        triangle(canvas, points[a], points[b], points[c])


drawing.makeImage("art.png", draw, pixelSize=(SIZE, SIZE), background=Color(1, 1, 1))