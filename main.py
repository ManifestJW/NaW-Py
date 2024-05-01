import pyglet

from assets import assetsInit
from assets import loadMenuStart

from events import on_draw

from RobberAI import generateRandomSeedRobber
from BearAI import generateRandomSeedBear

assetsInit()
generateRandomSeedRobber()
generateRandomSeedBear()
loadMenuStart()

pyglet.app.run()