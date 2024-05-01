import pyglet

import common
import colors

labels = []

class Rtext:
    def __init__(self, messrting, font, size, color, x, y, width, anchor_x, anchor_y, multiline):
        self.messrting = messrting
        self.font = font
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.multiline = multiline
    
    def create(self):
        label = pyglet.text.Label(self.messrting, font_name=self.font, font_size=self.size, color=self.color, x=self.x, y=self.y, width=self.width, anchor_x=self.anchor_x, anchor_y=self.anchor_y, multiline=self.multiline)
        return label

def assetsInit():
    icon = pyglet.image.load('assets\Img\WindowIcon.ico')
    common.gWindow.set_icon(icon)
    
    pyglet.font.add_directory('assets\Fonts')
    Pusab = pyglet.font.load('Pusab', 24)

    common.fps_display.label.font_name = 'Pusab'
    common.fps_display.label.x = 10
    common.fps_display.label.y = (common.SCRN_H - 10)
    common.fps_display.label.anchor_x = 'left'
    common.fps_display.label.anchor_y = 'top'


def createObj(messrting, font, size, color, x, y, width, anchor_x, anchor_y, multiline):
    tObj = Rtext(messrting, font, size, color, x, y, width, anchor_x, anchor_y, multiline)
    label = tObj.create()
    labels.append(label)
    del tObj

def freeLabels():
    labels.clear()

def loadMenuStart():
    createObj("Nightmare at Walmart", 'Pusab', 64, colors.white, 50, (common.SCRN_H - 50), None, 'left', 'top', False)
    createObj("New Game", 'Pusab', 48, colors.white, 90, (common.SCRN_H - 280), None, 'left', 'top', False)
    createObj("Continue", 'Pusab', 48, colors.white, 90, (common.SCRN_H - 340), None, 'left', 'top', False)
    createObj("Controls", 'Pusab', 48, colors.white, 90, (common.SCRN_H - 520), None, 'left', 'top', False)
    createObj("Settings", 'Pusab', 48, colors.white, 90, (common.SCRN_H - 580), None, 'left', 'top', False)
    createObj("Exit", 'Pusab', 48, colors.white, 90, (common.SCRN_H - 640), None, 'left', 'top', False)

def loadNewGame():
    createObj("I said I would never go back to Walmart, but I desperately need a job to support my family. The only job available is one at Walmart. I am not looking forward to it. There were... monsters. No one would believe me!", 'Pusab', 36, colors.white, 50, (common.SCRN_H - 50), 1180, 'left', 'top', True)
    createObj("Click To Continue", 'Pusab', 24, colors.white, (common.SCRN_W / 2), 50, None, 'center', 'top', False)