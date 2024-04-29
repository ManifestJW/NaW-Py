import pyglet

from pyglet import window
from pyglet import image
from pyglet import text
from pyglet import font

SCRN_W = 1280
SCRN_H = 720

ASPR_W = 16
ASPR_H = 9

gWindow = window.Window(SCRN_W, SCRN_H, "NaW")

white = (255, 255, 255, 255)

labels = []

def assetsInit():
    icon = image.load('assets\Img\WindowIcon.ico')
    gWindow.set_icon(icon)
    
    font.add_directory('assets\Fonts')
    Pusab = font.load('Pusab')

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
        label = text.Label(self.messrting, font_name=self.font, font_size=self.size, color=self.color, x=self.x, y=self.y, anchor_x=self.anchor_x, anchor_y=self.anchor_y)
        return label


def createObj(messrting, font, size, color, x, y, anchor_x, anchor_y):
    tObj = Rtext(messrting, font, size, color, x, y, anchor_x, anchor_y)
    label = tObj.create()
    labels.append(label)
    del tObj

def loadMenuStart():
    createObj("Nightmare at Walmart", 'Pusab', 64, white, 50, (SCRN_H - 50), 'left', 'center')

@gWindow.event
def on_draw():
    gWindow.clear()
    
    for x in range(len(labels)):
        labels[x].draw()