import pyglet

from common import *
from colors import *

labels = []

class Rtext:
    def __init__(self, messrting, font, size, color, x, y, anchor_x, anchor_y):
        self.messrting = messrting
        self.font = font
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
    
    def create(self):
        label = pyglet.text.Label(self.messrting, font_name=self.font, font_size=self.size, color=self.color, x=self.x, y=self.y, anchor_x=self.anchor_x, anchor_y=self.anchor_y)
        return label

def assetsInit():
    icon = pyglet.image.load('assets\Img\WindowIcon.ico')
    gWindow.set_icon(icon)
    
    pyglet.font.add_directory('assets\Fonts')
    Pusab = pyglet.font.load('Pusab', 24)

    fps_display.label.font_name = 'Pusab'
    fps_display.label.x = 10
    fps_display.label.y = (SCRN_H - 10)
    fps_display.label.anchor_x = 'left'
    fps_display.label.anchor_y = 'top'


def createObj(messrting, font, size, color, x, y, anchor_x, anchor_y):
    tObj = Rtext(messrting, font, size, color, x, y, anchor_x, anchor_y)
    label = tObj.create()
    labels.append(label)
    del tObj

def loadMenuStart():
    createObj("Nightmare at Walmart", 'Pusab', 64, white, 50, (SCRN_H - 50), 'left', 'top')
    createObj("New Game", 'Pusab', 48, white, 90, (SCRN_H - 280), 'left', 'top')
    createObj("Continue", 'Pusab', 48, white, 90, (SCRN_H - 340), 'left', 'top')
    createObj("Controls", 'Pusab', 48, white, 90, (SCRN_H - 520), 'left', 'top')
    createObj("Settings", 'Pusab', 48, white, 90, (SCRN_H - 580), 'left', 'top')
    createObj("Exit", 'Pusab', 48, white, 90, (SCRN_H - 640), 'left', 'top')