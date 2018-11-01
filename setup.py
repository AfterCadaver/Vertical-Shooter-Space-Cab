__author__ = 'kennichinitta'

'''
Initialize Display and create dictionaries of assets
'''

import os
import pygame as pg
from . import tools
from . import constants as c

GAME = 'BEGIN GAME'

ORIGINAL_CAPTION = 'Space Cab'

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(ORIGINAL_CAPTION)
DS = pg.display.set_mode(c.size)
DS_RECT = DS.get_rect()

FONTS = tools.set_fonts(os.path.join('assets', 'fonts'))
MUSIC = tools.set_music(os.path.join('assets', 'music'))
GFX   = tools.set_gfx(os.path.join  ('assets', 'gfx'))
SFX   = tools.set_sfx(os.path.join  ('assets', 'sfx'))
JSON  = tools.load_json(os.path.join('data'  , 'components'))


#FONT = pg.font.Font(FONTS[Fixedsys500c], 20) 
