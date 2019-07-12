from generativepy import drawing
from generativepy.drawing import Color, ROUND
from scipy.spatial import Delaunay
import random
import math


SIZE = 1000
N = 400

colors = [
    Color('white'),
    Color('black'),
    Color('lightgray'),
    Color('darkgray'),
    Color('lightgray'),
    ]

def triangle(canvas, a, b, c):
    color = random.choice(colors)
    #canvas.fill(color)
    canvas.stroke(Color('black'))
    canvas.strokeWeight(1)
    canvas.triangle(*a, *b, *c)


def draw(canvas):
    #random.seed(30)
    #randrange([start,] stop [,step])
    centerFactor = .25
    x_cord = (random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))))
    y_cord = (random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))))
    
    
    points_use = [(random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))), random.randrange((SIZE * centerFactor), (SIZE * (1-centerFactor))))
               for i in range(SIZE)]

    points_ = [(math.cos(i*2*math.pi/N), math.sin(i*2*math.pi/N)) for i in range(N)]
    
    b1 = 100
    b2 = 150
    h = 200
    area = ((b1 + b2)) / 2 * h
    num_of_points = 50
    points = [(random.randrange(area), random.randrange(area)) for i in range(num_of_points)]

    #print('points_rec', points_test)
    #print('points_cir', points_use)
    #points = [(x_cord, y_cord)
    #           for i in range(1000)]
    
    num_of_lines = 100
    for i in range(num_of_lines):  #[1,2,3,4,5...]
        #print('i = ', i)
        j = (i*15) % N
        #print('j= ', j)
        #print('unpack i: ', *points[i], ' unpack j: ', *points[j])
        canvas.line(*points_use[i], *points_use[j])


drawing.makeImage("custom.png", draw, pixelSize=(1000,1000), background=Color(1, 1, 1))