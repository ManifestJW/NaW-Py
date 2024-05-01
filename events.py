import pyglet
from pyglet.window import mouse

import common

from assets import labels
from assets import freeLabels
from assets import loadNewGame

from RobberAI import robberAI
from BearAI import bearAI
from BearAI import AiNum

def changeGameState(newGameState):
    common.gameState = newGameState

def startGame():
    pyglet.clock.schedule_interval(robberAI, 7)
    pyglet.clock.schedule_interval(bearAI, (-1 * (AiNum * 0.25)) + 7)

@common.gWindow.event
def on_mouse_press(x, y, button, modifier):
    if button == mouse.LEFT:
        if common.gameState == 'menu':
            if x >= labels[5].x and x <= labels[5].x + labels[5].content_width:
                if y <= labels[5].y and y >= labels[5].y - labels[5].content_height:
                    pyglet.app.exit()
            if x >= labels[1].x and x <= labels[1].x + labels[1].content_width:
                if y <= labels[1].y and y >= labels[1].y - labels[1].content_height:
                    freeLabels()
                    loadNewGame()
                    changeGameState("new")
        elif common.gameState == "new":
            freeLabels()
            startGame()
            changeGameState("in game")                

@common.gWindow.event
def on_draw():
    common.gWindow.clear()
    
    for x in range(len(labels)):
        labels[x].draw()
    
    common.fps_display.draw()