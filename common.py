import pyglet

SCRN_W = 1280
SCRN_H = 720

ASPR_W = 16
ASPR_H = 9

gameState = 'menu'

gWindow = pyglet.window.Window(SCRN_W, SCRN_H, "NaW")

fps_display = pyglet.window.FPSDisplay(window=gWindow, samples=100)