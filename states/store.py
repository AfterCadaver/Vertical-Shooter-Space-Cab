__author__ = 'AFTERCADAVER'

import json, os
import collections as collect
import pygame as pg
from .. import setup, tools, shopgui
from .. import constants as c


class shop(tools.State):
    '''
    THE STATE FOR THE
    SHOP
    '''
    def __init__(self):
        super(shop, self).__init__()
        self.font = pg.font.Font(setup.FONTS['cour'], 30)
        self.subscript = pg.font.Font(setup.FONTS['cour'], 20)
        self.volume = 0.4
        self.name = c.SHOP

    def startup(self,
                current_time,
                game_data):
        self.allow_input = False
        self.game_data = game_data
        self.index = 0
        self.list = self.make_list()
        self.position_list = self.make_height_list(self.list)
        self.selector_height = self.position_list[self.index]
        self.selected_item = self.make_list()[self.index]
        
        self.state_dict = self.make_state_dict()


        #COME BACK HERE AND CHANGE NAME
        
        self.width = 110

        self.number = 150
        self.gui = shopgui.Gui(self)
        
        self.state = c.SHOP

    def make_height_list(self, this_list):
        '''
        asdsasfsd
        '''
        that = []

        value = 40

        
        for items in this_list:
            that.append(value)

            value += 110

        return that

    def make_list(self):
        '''
        asdasfsadfg
        '''

        this_list = []

        y = 1

        for items in ['joy',
                      'spread',
                      'wave',
                      'special',
                      'missle',
                      'beam']:
            
            this_list.append(items + ' icon')

            y += 1

        return this_list

    def make_state_dict(self):

        '''
        MAKE DICTIONARY OF STATES IN LEVEL
        '''
        state_dict ={c.TRANSITION: self.transition,
                     c.SHOP:self.normal_update,
                     'ALL DONE':self.all_done
                    }

        return state_dict

    def transition(self,
                   surface,
                   keys,
                   current_time):

        #RENDER AND ANIMATE THE DOOR TRANSITION

        if self.number:
            self.number -= 1

        else:
            self.state = c.SHOP

    def go_back(self, surface,keys, current_time):

        #fsagdfg

        self.next = self.game_data['last level']
            
    def all_done(self,
                 surface,
                 keys,
                 current_time):
        '''
        asdaa
        '''

        text = 'ALL DONE?'

        # DRAW GREEN BOX FIRST HERE

        surface.blit(self.font.render(text,
                                      False,
                                      c.w),
                     (300,
                      400))

        if keys[pg.K_y]:
            self.done = True

        elif keys[pg.K_n]:
            self.state = c.SHOP

    def draw_level(self, surface):
        '''
        blit shop items
        '''

        #DRAW GUI

        self.gui.draw(surface)
        y = 50

        #LOOP OVER ITEMS IN LIST AND BLIT ONTO SURFACE
        
        for item in self.list:
            surface.blit(setup.GFX[item],
                         (150, y))

            surface.blit(self.font.render(
                         item[:-5],
                         True,
                         c.w),
                         (270, y))

            surface.blit(self.subscript.render(
                         item[:-5],
                         True,
                         c.w),
                         (270, y + 35))
            
            surface.blit(self.subscript.render(
                         item[:-5],
                         True,
                         c.w),
                         (270, y + 70))

            y += 110

        surface.blit(self.font.render(
                     str(self.game_data['points']),
                     True,
                     c.w),
                     (10,380))
        
        surface.blit(self.font.render('[x]BACK',
                                      True,
                                      c.w),
                                      (50, 750))
        
    def update(self, surface, keys, current_time):
        update_level = self.state_dict[self.state]
        update_level(surface,keys,current_time)

    def normal_update(self,
                      surface,
                      keys,
                      current_time):

                #SDFASFGFDAGDKH

        if self.allow_input:

            if keys[pg.K_UP]:
                self.index += -1
                self.allow_input = False
                
            if self.index < 0 and keys[pg.K_UP]:
                self.index += len(self.list)
                self.allow_input = False

            if keys[pg.K_DOWN]:
               self.index += 1
               self.allow_input = False
                    
            if self.index > len(self.list) - 1 and keys[pg.K_DOWN]:
                self.index += -len(self.list)
                self.allow_input = False

            self.selected_item = self.make_list()[self.index]

        #SWITCH BACK AND FORTH BETWEEN STATES

            if keys[pg.K_z]:
                self.game_data['points'] -= 170 
                self.game_data['weapon acquired'] = self.selected_item[:-5]
                self.allow_input = False

            if keys[pg.K_x]:
                self.next = 'menu'
                json.dump(self.game_data,
                          open('save.json','w'),
                          indent=7,
                          sort_keys=True)
                self.done = True

        if not keys[pg.K_UP] and not keys[pg.K_DOWN] and not keys[pg.K_z]:
            
            self.allow_input = True


        self.gui.selector.rect.y = self.position_list[self.index]

        surface.fill(c.b)
        
        self.draw_level(surface)
        
