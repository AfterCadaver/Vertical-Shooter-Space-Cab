__author__ = 'AFTERCADAVER'

import json
import collections as collect
import pygame as pg
from .. import setup, tools, shopgui, textbox
from .. import constants as c

class menu(tools.State):
    def __init__(self,
                 control):
        super(menu, self).__init__()
        self.volume = 0.4
        self.startup(0,0)
        self.state = c.NORMAL
        self.width = 30
        self.gui = shopgui.Gui(self)
        self.font = pg.font.Font(setup.FONTS['cour'], 30)
        self.next = 'shop'
        self.control = control

    def startup(self,
                current_time,
                game_data):

        self.game_data = game_data
        self.allow_input = False
        
        self.state_dict = self.make_state_dict()
        self.options = self.make_list()
        self.pos_list = self.make_pos_list()
        self.text_background = pg.Surface((550,160))
        
        self.index = 0
        
        self.selector_height = self.pos_list[self.index]
        self.selected_item = self.options[self.index]

    def make_list(self):

        option_list = ['shop',
                       'email',
                       'CONTINUE',
                       'QUIT']

        return option_list

    def make_pos_list(self):

        pos_list = [300,
                    330,
                    360,
                    390]

        return pos_list
        
    def make_state_dict(self):
        state_dict = {c.NORMAL:self.normal_update}

        return state_dict

    def draw_menu(self,
                  surface):
        
        surface.fill(c.w)

        index = 0

        surface.blit(self.text_background,(0,280))

        self.gui.draw(surface)

        for options in self.options:

            y = self.pos_list[index]

            surface.blit(self.font.render(options,
                                          True,
                                          c.w),
                         (20,y))
            index += 1

    def update(self,
               surface,
               keys,
               current_time):

        update_level = self.state_dict[self.state]
        update_level(surface,
                     keys,
                     current_time)

    def normal_update(self,
                      surface,
                      keys,
                      current_time):

        self.draw_menu(surface)

        self.selected_item = self.options[self.index]

        self.gui.selector.rect.y = self.pos_list[self.index]

        if self.allow_input:
            if keys[pg.K_UP]:
                self.index += -1
                self.allow_input = False

            if self.index < 0 and keys[pg.K_UP]:
                self.index += len(self.options)
                self.allow_input = False

            if keys[pg.K_DOWN]:
                self.index += 1
                self.allow_input = False

            if self.index > len(self.options) - 1 and keys[pg.K_DOWN]:
                self.index += -len(self.options)
                self.allow_input = False

            if keys[pg.K_z]:
                self.allow_input = False
                self.next = self.selected_item

                if self.selected_item == 'CONTINUE':
                    self.next = self.game_data['last level']

                if self.selected_item =='QUIT':
                    self.control.done = True

                self.done = True

        if not keys[pg.K_UP] and not keys[pg.K_DOWN] and not keys[pg.K_z]:            
            self.allow_input = True
