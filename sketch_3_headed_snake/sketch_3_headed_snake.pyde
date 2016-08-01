BOB=0
from random import *
def setup():
    size(1000,1000)
def draw():
    global BOB
    mouseX
    mouseY
    james= mouseX + 5
    dan= mouseY -5
    lauren= randrange(5,25)
    linda= randrange(5,26)
    BOB=randrange(0,256)
    jake= randrange(0,256)
    mike=randrange(0,256)
    fill (BOB, jake, mike)
    ellipse(mouseX, mouseY,lauren,linda)
    ellipse(james, dan, lauren, linda)
    ellipse( dan, james, lauren, linda)
    ellipse( dan, james, linda, lauren)
    ellipse(james,dan,linda, lauren)
    ellipse(mouseX, james, lauren, linda)
    ellipse(mouseY, mouseX, lauren, linda)
    