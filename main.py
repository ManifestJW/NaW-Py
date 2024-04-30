import pyglet

from assets import assetsInit
from assets import loadMenuStart

from events import on_draw

assetsInit()
loadMenuStart()
on_draw()

pyglet.app.run()