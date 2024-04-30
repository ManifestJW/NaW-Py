import pyglet

from common import *

from assets import labels

@gWindow.event
def on_draw():
    gWindow.clear()
    
    for x in range(len(labels)):
        labels[x].draw()
    
    fps_display.draw()