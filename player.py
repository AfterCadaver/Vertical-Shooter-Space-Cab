import json, os, math
import pygame as pg
from data import setup
from data import constants as c
from collections import deque

#PLAYER CLASS
class ship(pg.sprite.Sprite):
    def __init__(self,
                 group):
        pg.sprite.Sprite.__init__(self,
                                  group)
        self.image       = setup.GFX['ship']
        self.rect        = self.image.get_rect()
        self.speedx      = 0
        self.speedy      = 0
        self.energy      = 100
        self.reg_limit   = 100
        self.cur_weapon  = 'JOY'

    def controls(self):

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.speedx = -15

        if keys[pg.K_RIGHT]:
            self.speedx = 15

        if keys[pg.K_UP]:
            self.speedy  = -15

        if keys[pg.K_DOWN]:
            self.speedy = 15

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > 550:
            self.rect.right = 550

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > 800:
            self.rect.bottom = 800

        #gdfgdfgd

        if self.energy < self.reg_limit:
            self.energy += 0.2

        if self.energy < 50:
            self.reg_limit = 50

    def shoot(self):

        #FIRE PROJECTILES

        bullet = blasts((self.rect.centerx,
                        self.rect.top + 60),
                        self.weapon_equipped)

        self.energy -= 5

    def update(self):
        #SET SPEED TO ZERO IN ABSENCE OF PLAYER INPUT

        self.speedx = 0
        self.speedy = 0

        self.controls()

class blasts(pg.sprite.Sprite):
    """projectiles for the space cab"""
    def __init__(self,
                 pos,
                 name,
                 state='normal'):
        self.image        =  self.get_image[self.name]
        self.fill         =  self.image.fill(c.w)
        self.rect         =  self.image.get_rect(topleft=pos)
        self.speedy       =  -50

    def get_image(self):

        blast_dict = {'JOY':pg.Surface((6, 72)),
                      'TAZ':pg.Surface((6, 72))}

        return blast_dict

    def update(self):
        self.rect.bottom += self.speedy

        if self.rect.bottom <= 0:
            self.kill()
